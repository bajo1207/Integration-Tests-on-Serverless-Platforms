import requests
import pprint
import json
from flatten_dict import flatten
import csv

username = ''
password = ''
url = 'http://3.90.248.12:8080/'
jobs = []
for n in range(217,318):
    response = requests.get(f"{url}/job/aws-sam-dynamodb/{n}/wfapi", auth=(username, password))
    if response.ok:
        j = json.loads(response.text)
        jobs.append(j)
    else:
        break
data = [] 
pp = pprint.PrettyPrinter(indent=4)

for job in jobs:
    stageCheck = next((item for item in job['stages'] if item['name'] == 'Declarative: Checkout SCM'), None)
    stageSetup = next((item for item in job['stages'] if item['name'] == 'Build'), None)
    stageTest = next((item for item in job['stages'] if item['name'] == 'Test'), None)
    jobTime = {
        "jobId":job['id'],
        "duration":job['durationMillis'],
        "startTime":job['startTimeMillis'],
        "endTime":job['endTimeMillis']
    }
    if stageCheck:
        jobTime['stageCheck'] = {
            "duration":stageCheck['durationMillis'],
            "startTime":stageCheck['startTimeMillis']
        }
    if stageSetup:
        jobTime['stageSetup'] = {
            "duration":stageSetup['durationMillis'],
            "startTime":stageSetup['startTimeMillis']
        }
    if stageTest:
        jobTime['stageTest'] = {
            "duration":stageTest['durationMillis'],
            "startTime":stageTest['startTimeMillis']
        }
    data.append(jobTime)
pp.pprint(len(data))
with open('amazonLivedbTimes.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
