## How to install AWS CLI (Command Line Interface) on your local machine
(Linux machines)

* Download `.csv` key file of a user who has (for example) fully access to Amazon S3

Inside the key file, there're Access Key Id and Secret Access Key. We'll need those information.

* Download `aws-cli` by typing following commands

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

* Configure `aws-cli` by typing `aws configure`. 

You will be asked for Access Key Id and Secret Access Key, all are in the accessKeys .csv file. Copy paste. You will also be asked for default region, enter, for example, `eu-west-3` (Paris Region). Click Enter.

* To see if everything goes well, type:

```bash
aws s3api list-buckets --query 'Buckets[].Name'
```

This should display all your buckets inside amazon S3. 

## How to install AWS Python SDK

Use this command to install AWS Python SDK library on your machine:

```bash
pip install boto3
```

To install it with conda

```bash
conda install -c conda-forge boto3
```

Once you're done, try to run the following `python` script:

```python
import boto3
# use s3 service
s3 = boto3.resource('s3')
# print all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# upload file to s3
data = open('test.txt', 'rb')
s3.Bucket('your-bucket-name').put_object(Key='test.txt', Body=data)
```