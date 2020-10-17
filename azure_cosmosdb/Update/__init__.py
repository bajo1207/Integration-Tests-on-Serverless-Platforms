import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, cosmosdbOut: func.Out[func.Document], cosmosdbIn: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    if cosmosdbIn:
        data = json.loads(req.get_body())
        if 'text' not in data:
            logging.error("Validation Failed")
            raise Exception("Couldn't create the todo item.")
        item = json.loads(cosmosdbIn[0].to_json())
        item.update(data)
        cosmosdbOut.set(func.Document.from_json(json.dumps(item)))
        return func.HttpResponse(
                body=json.dumps(item),
                status_code=200, 
                headers={
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Access-Control-Allow-Methods": "OPTIONS,GET,PUT,POST,DELETE"
                }
            )
    else:
        return func.HttpResponse(
             "Todo not found",
             status_code=404
        )
