FROM python:latest
# Python 3.11+
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    libffi-dev libnacl-dev python3-dev jq

COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir install --upgrade pip
RUN pip3 --disable-pip-version-check --no-cache-dir install --user -r ./requirements.txt
RUN rm ./requirements.txt

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && rm -r awscliv2.zip
RUN ./aws/install

COPY ./aws_setting.sh ./
COPY ./config.json ./
RUN ./aws_setting.sh && rm ./config.json