import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, cosmosdb: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    if cosmosdb:
        items = []
        for todos in cosmosdb:
            items.append(json.loads(todos.to_json()))
        return func.HttpResponse(
                body= json.dumps(items),
                status_code=200, 
                headers={
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "OPTIONS,GET,PUT,POST,DELETE"
                }
            )
    else:
        return func.HttpResponse(
             "Todos not found",
             status_code=404
        )