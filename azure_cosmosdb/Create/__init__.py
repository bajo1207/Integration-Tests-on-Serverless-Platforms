import logging
import time
import uuid
import json
import azure.functions as func

def main(req: func.HttpRequest, cosmosdb: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    data = json.loads(req.get_body())
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    timestamp = str(time.time())

    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    cosmosdb.set(func.Document.from_json(json.dumps(item)))

    return func.HttpResponse(
        body=json.dumps(item),
        status_code=200, 
        headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,GET,PUT,POST,DELETE"
        }
    )