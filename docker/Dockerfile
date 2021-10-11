FROM amazonlinux
RUN yum update -y
RUN yum install -y python3
RUN pip3 install aitextgen
ADD train-input.txt .
ADD generate.py .
ADD train.py .
