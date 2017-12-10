FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install python-dateutil
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.nvidia=true
LABEL com.envoyai.schema-in="\
test-string: {type: 'string'}\n\
test-enum: {'enum': ['A', 'B', 'C']}\n\
test-date: {type: 'date-time'}\n\
test-bool: {type: 'boolean'}\n\
test-int: {type: 'integer'}\n\
test-float: {type: 'number', title: 'test-float'}\n\
test-percentage: {type: 'percentage'}\n\
test.zip: {mime-type: 'application/octet-stream'}\n\
test.jpg: {mime-type: 'image/jpeg'}\n\
test.pdf: {mime-type: 'application/pdf'}"
LABEL com.envoyai.schema-out="\
test-string: {type: 'string'}\n\
test-enum: {'enum': ['A', 'B', 'C']}\n\
test-date: {type: 'date-time'}\n\
test-bool: {type: 'boolean'}\n\
test-integer: {type: 'integer'}\n\
test-float: {type: 'number', title: 'test-float'}\n\
test-percentage: {type: 'percentage'}\n\
test.zip: {mime-type: 'application/octet-stream'}\n\
test.jpg: {mime-type: 'image/jpeg'}\n\
test.pdf: {mime-type: 'application/pdf'}"
LABEL com.envoyai.info="\
name: Echo Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"