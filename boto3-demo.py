import boto3
# use s3 service
s3 = boto3.resource('s3')

# upload file to s3
data = open('test.txt', 'rb')
s3.Bucket('foofoo123').put_object(Key='test/test.txt', Body=data)