FROM centos:latest

RUN yum install epel-release -y

RUN yum update -y

RUN yum install python3 -y

RUN yum install python3-pip -y

RUN pip3 install -U pip

RUN yum -y install libXext libSM libXrender 

RUN yum -y install gcc gcc-c++ python3-devel atlas atlas-devel gcc-gfortran openssl-devel libffi-devel 

RUN pip install --upgrade virtualenv

RUN virtualenv --system-site-packages ~/venvs/tensorflow

RUN source ~/venvs/tensorflow/bin/activate 

COPY tensorflow.txt /root/

RUN yum install net-tools -y

RUN pip install --upgrade -r /root/tensorflow.txt

CMD /bin/bash
