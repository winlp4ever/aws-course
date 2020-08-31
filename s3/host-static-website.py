import boto3
import json


s3 = boto3.client('s3')
s3_ = boto3.resource('s3')

region = 'eu-west-3'
bucket_name = 'my-static-website-123'

# check if a bucket with that name already exists
exists = True
try:
    s3_.meta.client.head_bucket(Bucket=bucket_name)
except botocore.exceptions.ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == '404':
        exists = False

if not exists:
    s3 = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

bucket_policy = {
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicRead",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::%s/*" % bucket_name
        }
    ]
}

# make the bucket publicly accessible
s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))

# define 2 principle pages
index = '''
<html>
    Hello world
</html>
'''
error = '''
<html>
    <h1> Oops!!! Error!</h1>
</html>
'''

# upload html files to s3
s3_.Bucket(bucket_name).put_object(Key='index.html', Body=index, ContentType='text/html')
s3_.Bucket(bucket_name).put_object(Key='error.html', Body=error, ContentType='text/html')


# Create the configuration for the website
website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

# Set the new policy on the selected bucket
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration=website_configuration
)