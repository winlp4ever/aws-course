import boto3

client = boto3.client('iam')

response = client.create_group(
    GroupName='foo'
)
response = client.attach_group_policy(
    GroupName='foo',
    PolicyArn='string'
)
print(response)