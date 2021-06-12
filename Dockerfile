#FROM ubuntu:18.04
FROM python:3.7

RUN apt-get update && \
    pip3 install --upgrade pip
COPY ./ /home/
RUN cd /home/ && \
    python3 setup.py install 
CMD sleep infinity

