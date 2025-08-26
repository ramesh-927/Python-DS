Q1: How do we connect kubernetes cluster eks or aks from your machine?

A:
Connecting EKS(Elestic Kubertnes services) or AKS(Azure Kubernetes Services) from a local mechine typically involves fowllowing steps.
1. Install Kubectl: The Kubernetes command line tool,"kubectl", is essential for intracting with any kubernetes cluster.
AKS : use Azure cli command : az aks install-cli ---> az aks get-credtials --resource-group <resource-group-name> --name <cluster-name>.. This command downloads the necessary credentials and updates your kubeconfig file.
EKS :   Use Aws cli  command :  aws eks update-kubeconfig --region <region> --name <cluster-name>. This command fetches the cluster inforamtion and updates your kubeconfig file to enable "kubectl" to connect. We need to ensure the AWS CLI installed and configured with apporiate persmissions.
2. Verify the connection: After configurating the credientials, verify the cluster using "kubectl". run kubectl get nodes.
    Impoart Considerations:
    1. Network Connectivity: Ensure the local mechine has network access to the EKS or AKS cluster end points. if the clsuter is in private network, you might need to use NAT( bastion hosts) or set up VPN host.
    2. Authentcation and Authorization: The credentials retrived in step2 grant you access based on the permissions assocaited with AWS IAM role or AZURE AD identity. ensure this identity has necassry permissions.
    3. Kubeconfig file:  the kubeconfig file (typically located at ~/ .kube/config) stores configurations for connecting to your kubernetes cluster.
-------------------------------------------------------------------------------------------------------------------------------
2Q: Can you tell me about the most recent versions of Azure Kubernetes Service (AKS) and Amazon Elastic Kubernetes Service (EKS) you’ve worked with? Additionally, could you explain how you utilize these versions during the provisioning process?

A:
 I've worked with AKS up to kubernetes 1.29 and EKS up to 1.30, the latest stable version in 2025.
For AKS, i use the Azure cli with az aks create, specifying --kubernetes-version 1.29, node count and VM size like Standard_D2s_v3. I enable the features like node Auto Provsioning wiht Karpenter for scaling, Azure container Service for volumes, and Azure monitor for observarbility. I ensure complaince with FIPS for sensetive workloads and plan upgrades using the AKS reader tracker.
For EKS, i provsion with eksctl or terraform,using --version 1.30. i leverage AWS Fargate for serverless workloads,configure CSI driver for EBS or EFS storages, and cluster autoscaler for autoscaling. i integrate for RBAC and cloudwathc for monitoring.
I choose AKS for Azure eco systems and quick setups and EKS for aws integration or serverless neeeds,ensurign autoscaling and complaince in both.
-------------------------------------------------------------------------------------------------------------------------------
3Q: Could you describe your experience with Continuous Deployment (CD) and the process you follow to deploy applications in a production environment?

A:
 I have extensive experience implmenting Continous Deployment Pipeline across AWS,Azure and kubernetes environments.My Typical process the code being pushed to a version control system like github and gitlab. A CI/CD tool such as jenkins, github actions, or harness automated unit, integration and security tests. if tests pass, the pipeline container images, store them in a registry and uses IaC tools helm or terraform for deployment.for production, i follow progressive delivery approach-blue/green or canary deployments- so we can validate a new vesrion with minmal user impact.i also intgrate obserbility like Prometheus, Datadog, and Splunk to monitor performance and roll back automatically if issues are detected. Security and approvals are built into the pipeline, ensuring compliance while still enabling fast, reliable releases.
-------------------------------------------------------------------------------------------------------------------------------
4Q: Can you explain the key components of Kubernetes and how the Container Network Interface (CNI) and Services work?

A:
Kubernetes consists of control plane components—API server, etcd, scheduler, and controller manager —and worker node components like kubelet, kube-proxy, and container runtime.The CNI plugin (like Calico, Flannel, or Cilium) handles pod networking by assigning each pod a unique IP and ensuring routing between pods across nodes, typically using overlay or BGP routing.This enables Kubernetes’ flat network model, where every pod can talk to every other pod without NAT. kube-proxy works with CNI to manage service IPs and routing rules.Kubernetes Services then abstract a set of pods, providing stable virtual IPs and DNS names.Depending on the type—ClusterIP, NodePort, LoadBalancer, or ExternalName—services ensure reliable pod discovery, load balancing, and external exposure, even when pods are dynamically created, scaled, or destroyed.
-------------------------------------------------------------------------------------------------------------------------------
5Q: Can you walk me through the step-by-step process you follow to upgrade a Kubernetes cluster?

A:
Upgrading Kubernetes is about minimizing downtime while keeping workloads safe. I usually follow these steps:
1. Plan & Backup – Review release notes, check deprecated APIs, back up etcd and manifests.
2. Upgrade Control Plane – Upgrade kubeadm, then update the API server, controller manager, scheduler, and etcd one node at a time.
3. Upgrade Worker Nodes – Upgrade kubelet and container runtime, then drain, upgrade, and uncordon each node sequentially to keep workloads running.
4. Upgrade Add-ons – Update CNI plugins, CoreDNS, Ingress controllers, and monitoring/logging agents.
5. Validation – Run health checks (kubectl get nodes/pods), verify workloads, and monitor with tools like Prometheus or Datadog.
6. Rollback Plan – Always keep a rollback path ready in case of failures.
I prefer doing upgrades in staging first, then production with rolling updates to ensure zero/minimal downtime.
Plan & Backup
# Check cluster version
kubectl version --short
# Check deprecated APIs
kubectl get apiservices
# Backup etcd (for kubeadm clusters)
ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/peer.crt \
  --key=/etc/kubernetes/pki/etcd/peer.key
2. Upgrade Control Plane
# Upgrade kubeadm
sudo apt-get update && sudo apt-get install -y kubeadm=1.xx.x-00
# Plan upgrade
sudo kubeadm upgrade plan
# Apply upgrade
sudo kubeadm upgrade apply v1.xx.x
3. Upgrade Worker Nodes
# Drain node
kubectl drain <node-name> --ignore-daemonsets
# Upgrade kubelet & kubectl
sudo apt-get update && sudo apt-get install -y kubelet=1.xx.x-00 kubectl=1.xx.x-00
sudo systemctl restart kubelet
# Uncordon node
kubectl uncordon <node-name>
4. Upgrade Add-ons
# Example: Upgrade CoreDNS
kubectl apply -f https://storage.googleapis.com/kubernetes-the-hard-way/coredns.yaml
# Example: Upgrade CNI plugin (Calico)
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
5. Validation
# Check nodes and pods
kubectl get nodes
kubectl get pods --all-namespaces
# Check cluster health
kubectl get cs  # componentstatuses
-------------------------------------------------------------------------------------------------------------------------------
6Q: Could you explain what multi-container pods are, their types, and how you would address a situation where one pod in a multi-container setup is consuming excessive CPU?

A:
Multi-container pods are Kubernetes pods that run more than one container within the same pod,sharing the same network namespace, storage volumes, and lifecycle.They’re typically used when containers need to work closely together.
There are three main design patterns:
1. Sidecar – a helper container (e.g., logging, monitoring, or proxy).
2. Ambassador – a container acting as a proxy to external services.
3. Adapter – a container that transforms or enriches data for the main application
If one container in a multi-container pod consumes excessive CPU, I would address it by:
1. Setting CPU requests and limits in the pod spec to prevent resource hogging.
2. Using cgroups and Kubernetes QoS classes to ensure fair resource allocation.
3. Monitoring with Prometheus/Datadog to identify which container is overusing CPU.
4. Optimizing the container process (code tuning, throttling, or offloading workloads).
5. If it’s an architectural issue, I’d consider splitting the workload into separate pods for better isolation and scaling.
This ensures the pod remains stable, and no single container impacts the performance of the others.
-------------------------------------------------------------------------------------------------------------------------------
7Q: How do you ensure the security of a Kubernetes cluster?

A:
Securing Kubernetes: To secure a Kubernetes cluster, I implement these key measures
1. RBAC & IAM: Use Role-Based Access Control with least-privilege roles and integrate with cloud IAM (e.g.Azure AD or AWS IAM)
2. Network Policies: Apply Calico or Cilium to restrict pod-to-pod communication, allowing only necessary traffic.
3. Secrets Management: Store sensitive data in Kubernetes Secrets or external vaults like HashiCorp Vault, and enable encryption at rest.
4. Pod Security: Use Pod Security Standards (PSS) to enforce runtime constraints and limit container privileges.
5. Image Security: Scan images with tools like AquaSec,Trivy and use trusted registries (e.g., ACR, ECR).
6. API Server Security: Enable TLS, disable anonymous access, and use audit logging.



