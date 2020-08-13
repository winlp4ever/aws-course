import boto3
# use s3 service
s3 = boto3.resource('s3')
response = client.add_user_to_group(
    GroupName='string',
    UserName='string'
)

# upload file to s3
data = open('text.txt', 'rb')
s3.Bucket('mypicture-1234').put_object(Key='txt.txt', Body=data, ContentType='text/plain')