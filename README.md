# Integration Tests on Serverless Platforms

A benchmark of different tools for integration testing in serverless.

* [aws_dynamodb](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/aws_dynamodb), [azure_cosmosdb](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/azure_cosmosdb) and [google_firestore](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/google_firestore) contains the respective todo applications and serverless frameworks for wich the bechmark was created.
The to do application is created as equally as possible for all the providers, as shown in the picture below.

* The applications is tested using jenkins continous integration server. The jenkins server can be found in [jenkins_container](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/jenkins_container).

* The python container used to execute the tests within the jenkins container can be found in [python_container](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/python_container).

* The analysis of the benchmark can be found in [data_analysis](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/data_analysis).

* The scripts to run the benchmark and get the data from the benchmark can be found in [benchmark_scripts](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/benchmark_scripts).

* A simple frontend to display the application can be found in [frontend](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/frontend).
The frontend is based on [this tutorial.](https://freshman.tech/todo-list/)

<img width="880" alt="" src="SampleApplication.png">

## Step by step guide to get everything working
1. First install the followinng tools: [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html), [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools) and [Functions Framework](https://cloud.google.com/functions/docs/functions-framework?hl=de)
1. Configure the three applications:
### AWS
1. First run the AWS build command: 
```{bash}
sam build --guided
``` 
Follow the instructions in the command line. All nessecary resources will be created.

2. Get credentials to access the created DynamoDB table in AWS. And put them in the docker-compose file in [jenkins_container](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/jenkins_container)

2. (Optional) If the emulated version of DynamoDB should be used, the following needs to be added to the Jenkins file in the buld stage:
```{bash}
 docker run --rm -d -p 8000:8000 --network dynamoNet --name dynamo amazon/dynamodb-local
 aws dynamodb create-table --cli-input-json file://create_todo_table.json --endpoint-url http://dynamo:8000
```
### Azure
1. Run the func init comand, and follow the instrunctions:
```{bash}
func init
```
2. Create a cosmos db database, with partition key = id
