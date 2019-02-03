import boto3
import os
from retrying import retry


def submit_query(query, database, s3_output):
    """Function for starting athena query"""
    client = boto3.client('athena')
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
            },
        ResultConfiguration={
            'OutputLocation': s3_output,
            'EncryptionConfiguration': {
                'EncryptionOption': 'SSE_KMS',
                'KmsKey': os.environ['KMSKEY']
                }
            }
        )
    print('Execution ID: ' + response['QueryExecutionId'])
    return response