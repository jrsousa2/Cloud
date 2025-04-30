# Snowflake, Databricks and cloud computing basics
**Reminder notes.**<br>

A quick reference on usage of simple Snowflake commands such as snowsql and snowsight.
<br>Also a quick compare of AWS and ACP services.


| Category                | AWS                                           | GCP                                              |
|-------------------------|-----------------------------------------------|--------------------------------------------------|
| Networking - VPC         | VPC                                           | VPC Network                                      |
| Compute                  | EC2                                           | Compute Engine                                   |
| Block Storage            | EBS                                           | Persistent Disks                                |
| Container Management     | ECS / EKS                                     | Cloud Run / GKE (Google Kubernetes Engine)       |
| Serverless Compute       | Lambda                                        | Cloud Functions                                  |
| Object Storage           | S3                                            | Cloud Storage                                    |
| File Storage             | EFS                                           | Filestore                                        |
| Load Balancer            | Elastic Load Balancing (ELB)                  | Cloud Load Balancing                             |
| DNS                      | Route 53                                      | Cloud DNS                                        |
| Database - Relational    | RDS                                           | Cloud SQL                                        |
| Database - NoSQL         | DynamoDB                                      | Firestore / Cloud Bigtable                       |
| Data Warehouse           | Redshift                                      | BigQuery                                         |
| Monitoring & Logging     | CloudWatch                                    | Cloud Monitoring & Logging (formerly Stackdriver)|
| Identity & Access        | IAM                                           | IAM                                              |
| DevOps - CI/CD           | CodePipeline / CodeBuild                      | Cloud Build / Cloud Deploy                       |
| Machine Learning         | SageMaker                                     | Vertex AI                                        |
| CDN                      | CloudFront                                    | Cloud CDN                                        |
| Secrets Management       | Secrets Manager                               | Secret Manager                                   |
| Infrastructure as Code   | CloudFormation                                | Deployment Manager / Terraform                   |
| Auto Scaling             | Auto Scaling Groups                           | Managed Instance Groups                          |
| API Management           | API Gateway                                   | API Gateway / Apigee                             |

** New **

| Category                | AWS                                           | GCP                                              | Azure                                |
|-------------------------|-----------------------------------------------|--------------------------------------------------|--------------------------------------|
| Networking - VPC         | VPC                                           | VPC Network                                      | Virtual Network (VNet)               |
| Compute                  | EC2                                           | Compute Engine                                   | Virtual Machines (VMs)               |
| Block Storage            | EBS                                           | Persistent Disks                                | Azure Disks                         |
| Container Management     | ECS / EKS                                     | Cloud Run / GKE                                  | Azure Kubernetes Service (AKS)      |
| Serverless Compute       | Lambda                                        | Cloud Functions                                  | Azure Functions                     |
| Object Storage           | S3                                            | Cloud Storage                                    | Azure Blob Storage                  |
| File Storage             | EFS                                           | Filestore                                        | Azure Files                         |
| Load Balancer            | Elastic Load Balancing (ELB)                  | Cloud Load Balancing                             | Azure Load Balancer                 |
| DNS                      | Route 53                                      | Cloud DNS                                        | Azure DNS                           |
| Database - Relational    | RDS                                           | Cloud SQL                                        | Azure SQL Database                  |
| Database - NoSQL         | DynamoDB                                      | Firestore / Cloud Bigtable                       | Azure Cosmos DB                     |
| Data Warehouse           | Redshift                                      | BigQuery                                         | Azure Synapse Analytics             |
| Monitoring & Logging     | CloudWatch                                    | Cloud Monitoring & Logging                       | Azure Monitor                       |
| Identity & Access        | IAM                                           | IAM                                              | Azure Active Directory (AAD)        |
| DevOps - CI/CD           | CodePipeline / CodeBuild                      | Cloud Build / Cloud Deploy                       | Azure DevOps / GitHub Actions       |
| Machine Learning         | SageMaker                                     | Vertex AI                                        | Azure Machine Learning              |
| CDN                      | CloudFront                                    | Cloud CDN                                        | Azure CDN                           |
| Secrets Management       | Secrets Manager                               | Secret Manager                                   | Azure Key Vault                     |
| Infrastructure as Code   | CloudFormation                                | Deployment Manager / Terraform                   | Azure Resource Manager (ARM) / Bicep|
| Auto Scaling             | Auto Scaling Groups                           | Managed Instance Groups                          | Virtual Machine Scale Sets (VMSS)    |
| API Management           | API Gateway                                   | API Gateway / Apigee                             | Azure API Management                |