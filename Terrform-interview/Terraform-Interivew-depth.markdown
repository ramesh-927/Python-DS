1. Q1. How frequently do you provision or update infrastructure using Terraform in your projects, and where do you store your Terraform configurations and state files?
Ans : In our projects, we typically provision infrastructure using Terraform when a new environment is created or when infrastructure changes are required, which can be anywhere from once a week to several times a sprint, depending on the release cycle.
All Terraform code is stored in a version-controlled Git repository, organized into environment-specific folders and reusable modules.
For state management, we use a remote backend — for example, AWS S3 with DynamoDB locking — so the state is consistent and accessible to the whole team, and we integrate Terraform plans/applies into our Jenkins pipelines with pull request approvals before deployment

2. Q2:  What types of applications have you deployed using Jenkins pipelines, and which deployment tools or strategies have you used?

Ans : In my recent projects, I’ve deployed a mix of Java Spring Boot microservices, Node.js APIs, and front-end React applications using Jenkins declarative pipelines.
For containerized workloads, I build Docker images and push them to ECR or ACR, then use Helm or Kustomize to deploy to Kubernetes clusters (EKS, AKS).
For cloud-native serverless apps, I use AWS CLI and SAM for Lambda deployments.
Infrastructure is provisioned via Terraform or AWS CDK within the pipeline, and for config management, I’ve integrated Ansible playbooks.
I’ve also implemented blue/green and canary deployment strategies with Jenkins pipelines, using AWS App Mesh and Kubernetes rolling updates to ensure zero downtime