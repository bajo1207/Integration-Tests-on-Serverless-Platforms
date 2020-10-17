import jenkins
import time

URL = 'http://3.90.248.12:8080/'
USERNAME = 'bajo1207'
PASSWORD = 'q5N634hyZvoI'
TIMEOUT = 120
SLEEP = 5
def get_job_info(j, JOB_NAME):
        return j.get_job_info(JOB_NAME)

def exit_if_job_running(job_info):
    print(job_info)
    if "queueItem" in job_info and job_info['queueItem'] != None:
        print("A job is already running")
        return -1
        
def get_last_build_number(j, JOB_NAME):
    info = get_job_info(j, JOB_NAME)
    if not info:
        return 0
    else:
        return info['lastBuild']['number'] + 1
        
def wait_for_job(j, build_number, timeout, JOB_NAME):
    timeout += 1
    if timeout > TIMEOUT:
        return None	
        
    try:
        build_info = j.get_build_info(JOB_NAME,build_number)
        if build_info['building']:
            time.sleep(SLEEP)
            return wait_for_job(j,build_number,timeout, JOB_NAME)
        return build_info
    except jenkins.JenkinsException:
        time.sleep(SLEEP)
        return wait_for_job(j,build_number,timeout, JOB_NAME)
def jenkins_run_job(JOB_NAME):   
    j = jenkins.Jenkins(URL, username=USERNAME, password=PASSWORD)
    build_number = get_last_build_number(j, JOB_NAME)

    print ("> RUNNING BUILD #%s ON %s%s" % (build_number,URL,JOB_NAME))
    j.build_job(JOB_NAME)
    build_info = wait_for_job(j,build_number,0, JOB_NAME)

    if build_info and build_info['result'] == 'FAILURE':
        return f"{build_number} ERROR"
    elif not build_info:
        return f"{build_number} ERROR"
    else:
        return f"{build_number} OK"


def main():
    """resultsAzure = []
    for number in range(10):
        try:
            resultsAzure.append(jenkins_run_job('azure-cosmosdb'))
        except:
            pass
    print(f"results Azure {resultsAzure}")
    print("#################################################################################################")"""
    resultsAmazon = []
    for number in range(110):
        try:
            resultsAmazon.append(jenkins_run_job('aws-sam-dynamodb'))
        except:
            pass
    print(f"results Amazon {resultsAmazon}")
    print("#################################################################################################")
    """resultsGoogle = []
    for number in range(10):
        try:
            resultsGoogle.append(jenkins_run_job('google-ff-fire'))
        except:
            pass
    print(f"results Google {resultsGoogle}")
    print("#################################################################################################")"""

if __name__ == "__main__":
    main()


