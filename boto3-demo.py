import boto3
# use s3 service
s3 = boto3.resource('s3')

# upload file to s3
data = open('text.txt', 'rb')
s3.Bucket('my-files-123').put_object(Key='text-files/text.txt', Body=data, ContentType='text/plain')
data.close()