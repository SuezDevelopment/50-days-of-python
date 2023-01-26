"""
A simple Python script that uses the AWS SDK for Python (Boto3) to list all the Amazon S3 buckets in your AWS account,
there are many more operations that can be performed using the boto3 library and different services provided by AWS.
"""

import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call the S3 service to list all the buckets
response = s3.list_buckets()

# Print the name of each bucket
for bucket in response['Buckets']:
    print(bucket['Name'])
