#CloudFormation Template To Provision EC2 Instance and Their Dependencies and Being used for Secure Web Hosting

##Problem:

Create a CloudFormation template that will create an EC2 instance and all required dependencies in a region that would allow only Alice and Bob to modify or login to, and only from their home IP addresses. Alice’s IP is 204.13.56.3 and Bob’s IP is 176.33.122.64. Alice and Bob will only be using SSH to communicate with the host, and the host is only being used for secure web hosting:
  - Template can be submitted in JSON or YAML formats.
  - You may only use SSH to communicate with the hosts.
  - Any web content being served from hosts MUST be secure content.

###Define Parameters required for EC2 instances:
  - Instance Type
  - EC2 Key Pair
  - Alice and Bob IP addresses

###Define what Region of AMI should be used to spin up EC2 instance

###Define EC2 dependencies:
    - VPC
    - Internet Gateway
    - Subnet
    - RouteTable and Routes and their associations to Subnet and Internet Gateway
    - Network ACL and InBound(Ingress) and OutBound(Egress) rules and subnet association
    - EC2 SecurityGroup

###Display Host Private IP to connect to host only by Alice and Bob

##Problem:

Create a Lambda function that could be used for compliance auditing, and would automatically review IAM User logins for corporate compliance. Lambda should be able to detect and automatically disable accounts not used or logged into for 90 days, and delete accounts not used or logged into for 180 days. Please use Java or Python as your development language.

###Python Lambda Function to review IAM users logins, disable IAM user profiles and delete IAM user accounts based on no of days inactivity
   - Using AWS Boto3 client pull IAM Users
   - Evaluate users login sessions based on timestamp
   - Pull IAM profiles and disable the users since not used accounts for more than 90 days
   - Delete the users since not used accounts for more than 180 days
