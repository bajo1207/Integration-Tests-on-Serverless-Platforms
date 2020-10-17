FROM python:3.8-buster
USER root
COPY google-ff-fire-049ca6dc6e71.json ./
COPY local.settings.json ./
RUN apt-get update && \
    apt-get -y --no-install-recommends install apt-transport-https \
      ca-certificates \
      curl \
      gnupg2 \
      software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
      $(lsb_release -cs) \
      stable" && \
    apt-get update && \
    apt-get -y --no-install-recommends install docker-ce && \
    apt-get clean
RUN pip install awscli \ 
    pip install aws-sam-cli \
    pip install pytest \
    pip install functions-framework
RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash -
RUN apt-get -y install nodejs
RUN npm i -g azure-functions-core-tools@3 --unsafe-perm true 