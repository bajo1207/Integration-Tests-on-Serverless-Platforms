# Integration Tests on Serverless Platforms

A benchmark of different tools for integration testing in serverless.

[aws_dynamodb](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/aws_dynamodb), [azure_cosmosdb](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/azure_cosmosdb) and [google_firestore](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/google_firestore) contains the respective todo applications and serverless frameworks for wich the bechmark was created.
The to do application is created as equally as possible for all the providers, as shown in the picture below.

The applications is tested using jenkins continous integration server. The jenkins server can be found in [jenkins_container](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/jenkins_container).

The python container used to execute the tests within the jenkins container can be found in [python_container](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/python_container).

The analysis of the benchmark can be found in [data_analysis](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/data_analysis).

The scripts to run the benchmark and get the data from the benchmark can be found in [benchmark_scripts](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/benchmark_scripts).

A simple frontend to test the application can be found in [frontend](https://github.com/bajo1207/Integration-Tests-on-Serverless-Platforms/tree/main/frontend) 

<img width="880" alt="" src="SampleApplication.png">
