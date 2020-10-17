import logging
import os
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
     logging.info(f'Python HTTP trigger function processed a request.')
     cosmosDbUrl = os.environ["cosmosurl"]
     cosmosDbKey = os.environ["cosmoskey"]
     client = CosmosClient(cosmosDbUrl, credential=cosmosDbKey)
     database_name = 'todos-python'
     database = client.get_database_client(database_name)
     container_name = 'todos-python-container'
     container = database.get_container_client(container_name)
     itemId = req.route_params['id']
     try:
          container.delete_item(item=itemId, partition_key=itemId)
     except:
          return func.HttpResponse(
             "Todo not found",
             status_code=404
        )
     
     return func.HttpResponse(f"Hello,. This HTTP triggered function executed successfully.")