import boto3
from pprint import pprint
import boto3.session
aws_management_console = boto3.session.Session(profile_name="default")
ec2_console = aws_management_console.client(service_name="ec2", region_name="ap-south-1")
result = ec2_console.describe_instances()['Reservations']
# print(result)
# pprint(result)
for each_instances in result:
  for value in each_instances['Instances']:
    print(value['InstanceId'])