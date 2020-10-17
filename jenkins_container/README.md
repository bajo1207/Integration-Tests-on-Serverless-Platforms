docker build -t jenkins-docker .

docker run -it -p 8080:8080 -p 50000:50000 -v /home/bajo1207/testplace:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --restart unless-stopped jenkins-docker