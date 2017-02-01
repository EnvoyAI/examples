FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install simplejson python-dateutil
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []