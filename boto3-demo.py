import boto3
# use s3 service
s3 = boto3.resource('s3')
# print all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# upload file to s3
data = open('test.txt', 'rb')
s3.Bucket('mypicture-123').put_object(Key='test/test.txt', Body=data)