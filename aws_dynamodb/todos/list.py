import json
import os
from decimalencoder import DecimalEncoder
import boto3
dynamodb = boto3.resource('dynamodb')

def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan()

    # create a response
    response = {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,GET,PUT,POST,DELETE"
        },
        "body": json.dumps(result['Items'], cls=DecimalEncoder)
    }

    return response
