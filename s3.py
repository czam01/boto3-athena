import boto3
import sys
import botocore


region = sys.argv[1]

s3 = boto3.client(
  's3',
  region_name = region
)

response = s3.list_buckets()
print (response)
