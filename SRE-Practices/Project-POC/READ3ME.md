

1. Build a tiny **TypeScript “Hello World”** web app.
2. Containerize it (Docker).
3. Push the image to **AWS ECR**.
4. Deploy it to **ECS Fargate**.
5. Show an **Azure DevOps (ADO) YAML pipeline** that builds, pushes and deploys (uses your free ADO + AWS credentials).
____________________________________________________________

* Write a tiny Node/TypeScript app that returns “Hello World” when you open a web page.
* Package that app into a Docker image (like zipping the app into a standard box).
* Upload that image to AWS ECR (a private image storage on AWS).
* Tell ECS Fargate (AWS service that runs containers) to run that image.
* Then you automate steps 2–4 with an Azure DevOps YAML pipeline that runs whenever you push code.

-------------------------------------------------------------------

Local Mac : Node + Docker + AWS CLI installed.
AWS : ECR repository (to hold image), ECS cluster + service (Fargate) to run it, and a small IAM role so ECS can pull the image & write logs.
Azure DevOps: store AWS creds securely (pipeline variables or service connection) and run the YAML pipeline to build/push/deploy.

Helpful doc references :-

* Authenticate docker to ECR (how to login & push). [AWS Documentation]
* Register ECS task definitions (how ECS knows which image to run). [AWS Documentation]
* Full AWS CLI Fargate walkthrough (create cluster, register task, run). [AWS Documentation]
* How to create service connections / pipeline variables in Azure DevOps. [Microsoft Learn]
* A short guide to set up Node + Express + TypeScript (Hello World). [LogRocket Blog]

---

# Prerequisites (what to install on your Mac)

1. Homebrew (if you don’t have it): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Node.js (v18+) and npm: `brew install node`
3. Docker Desktop for Mac — install and run Docker Desktop app (GUI).
4. AWS CLI v2: `brew install awscli` (then run `aws --version`)
5. (Optional) jq for JSON manipulation: `brew install jq`

Also create (or have) accounts:

* AWS account (you can use free tier credentials). Configure locally: `aws configure` and enter your AWS Access Key / Secret / Region.
* Azure DevOps account/project (free tier is fine). You’ll later add AWS credentials as secure pipeline variables or a service connection.

---

# Folder & file layout (what you’ll create)

Create a folder for the POC:

```
hello-ecs-poc/
├─ src/
│  └─ index.ts
├─ package.json
├─ tsconfig.json
├─ Dockerfile
├─ .dockerignore
├─ taskdef.json.template
└─ azure-pipelines.yml
```

---

# 1) Create the TypeScript "Hello World" app (local test)

Create `package.json`:

```json
{
  "name": "hello-ts",
  "version": "0.1.0",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "@types/express": "^4.17.17"
  }
}
```

Create `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "CommonJS",
    "outDir": "dist",
    "esModuleInterop": true,
    "strict": true
  },
  "include": ["src"]
}
```

Create `src/index.ts`:

```ts
import express from 'express';
const app = express();
const port = process.env.PORT ? Number(process.env.PORT) : 3000;

app.get('/', (req, res) => {
  res.send('Hello World from TypeScript container!');
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

Install & build locally:

```bash
npm install
npm run build
node dist/index.js
# Then open http://localhost:3000 — you should see "Hello World..."
```

(That shows the app works locally before we containerize it.)

---

# 2) Dockerize the app (Dockerfile + local test)

Create `.dockerignore`:

```
node_modules
dist
npm-debug.log
.git
```

Create a **multi-stage** `Dockerfile` (small final image):

```Dockerfile
# build stage
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY tsconfig.json ./
COPY src ./src
RUN npm run build

# runtime stage
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=build /app/dist ./dist
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

Build and run locally:

```bash
docker build -t hello-ts:0.1 .
docker run --rm -p 3000:3000 hello-ts:0.1
# visit http://localhost:3000 again
```

---

# 3) Create an ECR repo and push your image

(You can do these with AWS Console or AWS CLI. Below are CLI commands — replace `us-east-1` with your region.)

Create repository:

```bash
aws ecr create-repository --repository-name hello-ts --region us-east-1
```

Find your AWS account id:

```bash
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=us-east-1
REPO_URI=${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/hello-ts
```

Login Docker to ECR (this is the correct modern command — it returns a password and pipes to docker):

```bash
aws ecr get-login-password --region $REGION \
  | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com
```

(Official AWS docs describe this `get-login-password` approach.) ([AWS Documentation][1])

Tag & push:

```bash
IMAGE_TAG=v1
docker tag hello-ts:0.1 ${REPO_URI}:${IMAGE_TAG}
docker push ${REPO_URI}:${IMAGE_TAG}
```

If the push succeeds, your image is now in ECR.

---

# 4) Prepare IAM role required for ECS (task execution role)

ECS Fargate tasks need a small **execution role** so AWS can pull the image and send logs to CloudWatch. You can create it in the console, or with CLI:

Create a trust policy file `task-exec-trust.json`:

```json
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Principal":{"Service":"ecs-tasks.amazonaws.com"},
      "Action":"sts:AssumeRole"
    }
  ]
}
```

Create the role and attach the managed policy:

```bash
aws iam create-role --role-name ecsTaskExecutionRole --assume-role-policy-document file://task-exec-trust.json
aws iam attach-role-policy --role-name ecsTaskExecutionRole --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
```

(Documentation: ECS task execution role details — required so Fargate can pull from ECR and publish logs.) [AWS Documentation]

---

# 5) Create cluster & register a task definition for Fargate

Create cluster:

```bash
aws ecs create-cluster --cluster-name hello-cluster
```

Create `taskdef.json.template` (a simple template — later pipeline will replace `IMAGE_URI` with the real image URI & tag):

```json
{
  "family": "hello-task",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::ACCOUNT_ID:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "hello",
      "image": "IMAGE_URI",
      "portMappings": [
        { "containerPort": 3000, "protocol": "tcp" }
      ],
      "essential": true
    }
  ]
}
```

Notes: replace `ACCOUNT_ID` with your numeric account id, and `IMAGE_URI` will be replaced by pipeline (or CLI step) with `${REPO_URI}:v1`. See AWS docs for example task definitions. ([AWS Documentation][7])

Register and deploy (example CLI flow — you can run locally to test once the image is in ECR):

```bash
# Replace placeholder with real image URI
sed "s|IMAGE_URI|${REPO_URI}:${IMAGE_TAG}|g" taskdef.json.template > taskdef.json

# register task definition
aws ecs register-task-definition --cli-input-json file://taskdef.json

# create a service (first time)
aws ecs create-service \
  --cluster hello-cluster \
  --service-name hello-service \
  --task-definition hello-task \
  --desired-count 1 \
  --launch-type FARGATE \
  --network-configuration 'awsvpcConfiguration={subnets=["subnet-abc..."],securityGroups=["sg-abc..."],assignPublicIp="ENABLED"}'
```

Important: For Fargate `--network-configuration` you must pass valid VPC subnets and security group(s) that allow inbound on port 3000 (or use public subnets + a security group that allows inbound from 0.0.0.0/0 for testing).

If you want a simpler CLI workflow, AWS docs show how to do this end-to-end with the CLI. ([AWS Documentation][3])

---

# 6) Azure DevOps YAML pipeline (automate build → push → deploy)

Below is a **complete** `azure-pipelines.yml` you can put at repo root. The pipeline:

* Installs Node, builds TypeScript.
* Builds Docker image, logs into ECR, pushes image.
* Registers task definition and updates ECS service to force new deployment.

> **Security note:** do **not** hardcode your AWS keys in the YAML. Add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as secret pipeline variables in the ADO UI (or use an AWS service connection). See Azure docs on service connections and pipeline variables. ([Microsoft Learn][4])

`azure-pipelines.yml`:

```yaml
trigger:
  - main

variables:
  AWS_REGION: 'us-east-1'
  ECR_REPO: 'hello-ts'
  ECS_CLUSTER: 'hello-cluster'
  ECS_SERVICE: 'hello-service'
  TASK_FAMILY: 'hello-task'

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: NodeTool@0
  inputs:
    versionSpec: '18.x'
  displayName: 'Use Node 18'

- script: |
    npm ci
    npm run build
  displayName: 'Install & build'

- script: |
    IMAGE_TAG=$(Build.BuildId)
    docker build -t ${ECR_REPO}:$IMAGE_TAG .
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    REPO_URI=${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}
    docker tag ${ECR_REPO}:$IMAGE_TAG ${REPO_URI}:$IMAGE_TAG
    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${REPO_URI}
    docker push ${REPO_URI}:$IMAGE_TAG
    # prepare taskdef.json from template
    sed "s|IMAGE_URI|${REPO_URI}:${IMAGE_TAG}|g" taskdef.json.template > taskdef.json
    aws ecs register-task-definition --cli-input-json file://taskdef.json
    aws ecs update-service --cluster ${ECS_CLUSTER} --service ${ECS_SERVICE} --force-new-deployment
  env:
    AWS_ACCESS_KEY_ID: $(AWS_ACCESS_KEY_ID)
    AWS_SECRET_ACCESS_KEY: $(AWS_SECRET_ACCESS_KEY)
  displayName: 'Build, push to ECR and deploy to ECS'
```

In Azure DevOps portal → create a new Project.

Go to Repos → Clone or Push existing code.

On your Mac, from your hello-ecs-poc folder:

bash
git init
git remote add origin <ADO_repo_clone_URL>
git add .
git commit -m "Initial commit - Hello ECS Fargate POC"
git push -u origin main
Now all your files (index.ts, Dockerfile, taskdef.json.template, azure-pipelines.yml) are in ADO.

2️⃣ Create AWS credentials in ADO (securely)
We don’t hardcode AWS keys in the YAML — instead, store them as secret variables.

In ADO → Pipelines → Library → + Variable group (or directly in the pipeline UI).

Add:
Alternatively:
Use Service connections → Add AWS → enter your keys → give it a name like aws-connection. Then in YAML, you can use AWS DevOps tasks with that service connection.
or 
-----
AWS_ACCESS_KEY_ID → paste your key, click Keep this value secret.

AWS_SECRET_ACCESS_KEY → paste secret key, mark as secret.

Optionally AWS_REGION = us-east-1 (non-secret).

Save the variable group and link it to the pipeline (in pipeline settings).



3️⃣ Create the pipeline in ADO
In ADO → Pipelines → New Pipeline.

Choose Azure Repos Git → select your repo.

Select Existing Azure Pipelines YAML file → point to azure-pipelines.yml in your repo.


Add an Install AWS CLI step if it’s not preinstalled:

yaml

- script: |
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
  displayName: 'Install AWS CLI'
(You can skip this if the hosted agent already has AWS CLI v2.)

5️⃣ Run the pipeline
Commit & push changes → ADO will trigger automatically (because of trigger: - main).

The log will show:

Node install + TypeScript build.

Docker build & push to ECR.

ECS task definition registration.

ECS service update → new container version running in Fargate.

6️⃣ Verify deployment in AWS console
Go to:

ECR → check your repo → new image tag exists.

ECS → cluster → service → tasks → check logs.

Open the service’s public IP in browser → you should see "Hello World from TypeScript container!".

