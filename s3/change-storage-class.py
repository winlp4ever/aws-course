import boto3

s3 = boto3.client('s3')

copy_source = {
    'Bucket': 'mybucket',
    'Key': 'mykey'
}

s3.copy(
  copy_source, 'mybucket', 'mykey',
  ExtraArgs = {
    'StorageClass': 'STANDARD_IA',
    'MetadataDirective': 'COPY'
  }
)