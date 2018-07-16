FROM ubuntu:16.04

RUN sed -i -s 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
  python python-pip

RUN pip install -U \
    pip \
    robotframework==3.0.2 \
    robotframework-selenium2library==1.8.0 \
    selenium==2.53.6 \
    robotframework-ftplibrary \
    robotframework-excellibrary==0.0.2 \
    robotframework-requests==0.4.7
