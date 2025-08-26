Q1. How do we connect kubernetes cluster eks or aks from your machine?

Answer :- Connecting EKS(Elestic Kubertnes services) or AKS(Azure Kubernetes Services) from a local mechine typically involves fowllowing steps.
    1. Install Kubectl: The Kubernetes command line tool,"kubectl", is essential for intracting with any kubernetes cluster.
        AKS : use Azure cli command : az aks install-cli ---> az aks get-credtials --resource-group <resource-group-name> --name <cluster-name>.. This command downloads the necessary credentials and updates your kubeconfig file.

        EKS :   Use Aws cli  command :  aws eks update-kubeconfig --region <region> --name <cluster-name>. This command fetches the cluster inforamtion and updates your kubeconfig file to enable "kubectl" to connect. We need to ensure the AWS CLI installed and configured with apporiate persmissions.
    2. Verify the connection: After configurating the credientials, verify the cluster using "kubectl".
        run kubectl get nodes.
Impoart Considerations:
    1. Network Connectivity: Ensure the local mechine has network access to the EKS or AKS cluster end points. if the clsuter is in private network, you might need to use NAT( bastion hosts) or set up VPN host.
    2. Authentcation and Authorization: The credentials retrived in step2 grant you access based on the permissions assocaited with AWS IAM role or AZURE AD identity. ensure this identity has necassry permissions.
    3. Kubeconfig file:  the kubeconfig file (typically located at ~/ .kube/config) stores configurations for connecting to your kubernetes cluster.
-------------------------------------------------------------------------------------------------------------------------------

2Q. Can you tell me about the most recent versions of Azure Kubernetes Service (AKS) and Amazon Elastic Kubernetes Service (EKS) you’ve worked with? Additionally, could you explain how you utilize these versions during the provisioning process?

Answer :- I've worked with AKS up to kubernetes 1.29 and EKS up to 1.30, the latest stable version in 2025.
For AKS, i use the Azure cli with az aks create, specifying --kubernetes-version 1.29, node count and VM size like Standard_D2s_v3. I enable the features like node Auto Provsioning wiht Karpenter for scaling, Azure container Service for volumes, and Azure monitor for observarbility. I ensure complaince with FIPS for sensetive workloads and plan upgrades using the AKS reader tracker.
For EKS, i provsion with eksctl or terraform,using --version 1.30. i leverage AWS Fargate for serverless workloads,configure CSI driver for EBS or EFS storages, and cluster autoscaler for autoscaling. i integrate for RBAC and cloudwathc for monitoring.

I choose AKS for Azure eco systems and quick setups and EKS for aws integration or serverless neeeds,ensurign autoscaling and complaince in both.
-------------------------------------------------------------------------------------------------------------------------------

3Q. Could you describe your experience with Continuous Deployment (CD) and the process you follow to deploy applications in a production environment?

Answer:- I have extensive experience implmenting Continous Deployment Pipeline across AWS,Azure and kubernetes environments.My Typical process the code being pushed to a version control system like github and gitlab. A CI/CD tool such as jenkins, github actions, or harness automated unit, integration and security tests. if tests pass, the pipeline container images, store them in a registry and uses IaC tools helm or terraform for deployment.for production, i follow progressive delivery approach-blue/green or canary deployments- so we can validate a new vesrion with minmal user impact.i also intgrate obserbility like Prometheus, Datadog, and Splunk to monitor performance and roll back automatically if issues are detected. Security and approvals are built into the pipeline, ensuring compliance while still enabling fast, reliable releases.
-------------------------------------------------------------------------------------------------------------------------------
