FROM apache/flink:1.18.0

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && \
    ln -sf /usr/bin/python3 /usr/bin/python

RUN pip3 install apache-flink==1.18.0