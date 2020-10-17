from invoke import task

@task
def start(c):
    with open('data.txt', 'a') as outfile:
        outfile.write("[")
        while True:
            print("###############################################################")
            dockerstats = c.run('docker stats --no-stream --format "{{ json .}}"').stdout
            print("##################################################################")
            timestamp = str(time.time())
            stats = dockerstats.splitlines()
            for stat in stats:
                statObj = json.loads(stat)
                statObj['timestamp'] = timestamp
                json.dump(statObj, outfile, indent=4)
                outfile.write(",")
            time.sleep(1)