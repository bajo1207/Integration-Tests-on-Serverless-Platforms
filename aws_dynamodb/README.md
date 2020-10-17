# Integration testing a python-rest-api on AWS with AWS SAM

docker run -d -p 8000:8000 --network dynamoNet --name dynamo amazon/dynamodb-local

aws dynamodb create-table --table-name TodoTable --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 --endpoint-url http://localhost:8000