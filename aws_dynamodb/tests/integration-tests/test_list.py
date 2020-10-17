import boto3
import botocore
import json
import pytest


def test_list():
    # Set "running_locally" flag if you are running the integration test locally
    running_locally = True
    if running_locally:
        # Create Lambda SDK client to connect to appropriate Lambda endpoint
        lambda_client = boto3.client('lambda',
            region_name="us-east-1",
            endpoint_url="http://localhost:3001",
            use_ssl=False,
            verify=False,
            config=botocore.client.Config(
                signature_version=botocore.UNSIGNED,
                read_timeout=10,
                retries={'max_attempts': 4},
            )
        )
    else:
        lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName="ListFunction",
        InvocationType="RequestResponse")
    responsePayload = json.loads(response['Payload'].read().decode())
    print(responsePayload)

    assert responsePayload['statusCode'] == 200