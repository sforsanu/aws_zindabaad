#import the module
import boto3
from pprint import pprint  #this is used to get the information structured format 
import boto3.session
#open management console
aws_management_console = boto3.session.Session(profile_name="default")
#open iam console
iam_console = aws_management_console.client(service_name= "iam")
#list the users
result = iam_console.list_users()
pprint(result)
for each_user in result['Users']:
  print(each_user['UserName'])
  