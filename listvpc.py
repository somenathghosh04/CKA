import boto3
import re
import botocore.session
session = botocore.session.get_session()
client = session.create_client('sts')
res = client.get_session_token()

access_key = res['Credentials']['AccessKeyId']
secret_access_key = res['Credentials']['SecretAccessKey']
session_token = res['Credentials']['SessionToken']

# print(res)

print('ACCESS_KEY ', access_key)
print('SECRET-ACCESS_KEY ', secret_access_key)
print('SESSION_TOKEN', session_token)





