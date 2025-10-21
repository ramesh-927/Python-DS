Create a Hello World container app, push the image to ECR, and deploy it to ECS Fargate. Use the free credentials available with ADO (for Pipeline) and AWS for this exercise.
Instructure code should be in Type script. ADO pipeline should be YML and should not be classsic

Breakdown of POC:

Here’s a complete, ready-to-run Hello World TypeScript container + instructions to push to ECR and deploy to ECS Fargate, plus a non-classic Azure DevOps YAML pipeline that builds the image and performs the push & deployment. I’ll give you all code files, the CLI commands you’ll run once, and the ADO pipeline YAML (no classic pipelines)

1. Hello World Containaer app(TypeScript).
2. Build + push to AWS ECR
3. Deploy to AWS ECS Fargate
4. Infrastructure code in TypeScript(CDK)
5. Azure DevOps pipeline in YAML(no clasic) to auotmate  build/push/deploy


______
Folder structre: 

hello-ecs-poc/
├─ src/
│  └─ index.ts
├─ package.json
├─ tsconfig.json
├─ Dockerfile
├─ .dockerignore
├─ taskdef.json.template
└─ azure-pipelines.yml

1) Create the TypeScript "Hello World" app (local test)
Create tsconfig.json:
Create src/index.ts:

--Install & build locally:
npm install
npm run build
node dist/index.js
_____________
2) Dockerize the app (Dockerfile + local test)
Create .dockerignore:
Create a multi-stage Dockerfile (small final image):

docker build -t hello-ts:0.1 .
docker run --rm -p 3000:3000 hello-ts:0.1
# visit http://localhost:3000 again
____________________
3) Create an ECR repo and push your image
Create repository:
aws ecr create-repository --repository-name hello-ts --region us-east-1


2. AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=us-east-1
REPO_URI=${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/hello-ts
Find your AWS account id:
https://us-east-1.console.aws.amazon.com/ecr/private-registry/repositories?region=us-east-1 
----
Login Docker to ECR (this is the correct modern command — it returns a password and pipes to docker):
 aws ecr get-login-password --region $REGION \
  | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

Login Succeeded

Tag & push:

IMAGE_TAG=v1
docker tag hello-ts:0.1 ${REPO_URI}:${IMAGE_TAG}
docker push ${REPO_URI}:${IMAGE_TAG}
______________________

4) Prepare IAM role required for ECS (task execution role)

Create a trust policy file task-exec-trust.json:

aws iam create-role --role-name ecsTaskExecutionRole --assume-role-policy-document file://task-exec-trust.json
aws iam attach-role-policy --role-name ecsTaskExecutionRole --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
__(Documentation: ECS task execution role details — required so Fargate can pull from ECR and publish logs.)

____________________________________________

5) Create cluster & register a task definition for Fargate
Create cluster
Note: replace ACCOUNT_ID with your numeric account id, and IMAGE_URI will be replaced by pipeline (or CLI step) with ${REPO_URI}:v1
####
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

####
Important: For Fargate --network-configuration you must pass valid VPC subnets and security group(s) that allow inbound on port 3000 (or use public subnets + a security group that allows inbound from 0.0.0.0/0 for testing).