
Push your project to Azure DevOps repo
In Azure DevOps portal → create a new Project.

Go to Repos → Clone or Push existing code.
 from your hello-ecs-poc folder:

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

AWS_ACCESS_KEY_ID → paste your key, click Keep this value secret.

AWS_SECRET_ACCESS_KEY → paste secret key, mark as secret.

Optionally AWS_REGION = us-east-1 (non-secret).

Save the variable group and link it to the pipeline (in pipeline settings).

📌 Alternatively:
Use Service connections → Add AWS → enter your keys → give it a name like aws-connection. Then in YAML, you can use AWS DevOps tasks with that service connection.

