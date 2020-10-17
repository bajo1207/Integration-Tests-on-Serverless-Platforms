import logging
import azure.functions as func

def main(req: func.HttpRequest, cosmosdb: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    if cosmosdb:
        item = cosmosdb[0]
        return func.HttpResponse(
                body=item.to_json(),
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
