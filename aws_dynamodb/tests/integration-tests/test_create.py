import boto3
import botocore
import json
import pytest


def test_create():
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
    payload = {"body":"{\"text\":\"This is a sample texta\"}"}
    jsonpayload = json.dumps(payload)
    response = lambda_client.invoke(
        FunctionName="CreateFunction",
        InvocationType="RequestResponse",
        Payload=bytes(jsonpayload, encoding="utf-8"))
    responsePayload = json.loads(response['Payload'].read().decode())

    assert responsePayload['statusCode'] == 200