FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install python-dateutil
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.nvidia=false
LABEL com.envoyai.schema-in="\
test-string: {type: 'string', nullable: true}\n\
test-enum: {'enum': ['A', 'B', 'C'], nullable: true}\n\
test-date: {type: 'date-time', nullable: true}\n\
test-bool: {type: 'boolean', nullable: true}\n\
test-int: {type: 'integer', nullable: true}\n\
test-float: {type: 'number', nullable: true}\n\
test-percentage: {type: 'percentage', nullable: true}\n\
test.zip: {mime-type: 'application/octet-stream', nullable: true}\n\
test.jpg: {mime-type: 'image/jpeg', nullable: true}\n\
test.pdf: {mime-type: 'application/pdf', nullable: true}"
LABEL com.envoyai.schema-out="\
test-string: {type: 'string', nullable: true}\n\
test-enum: {'enum': ['A', 'B', 'C'], nullable: true}\n\
test-date: {type: 'date-time', nullable: true}\n\
test-bool: {type: 'boolean', nullable: true}\n\
test-int: {type: 'integer', nullable: true}\n\
test-float: {type: 'number', nullable: true}\n\
test-percentage: {type: 'percentage', nullable: true}\n\
test.zip: {mime-type: 'application/octet-stream', nullable: true}\n\
test.jpg: {mime-type: 'image/jpeg', nullable: true}\n\
test.pdf: {mime-type: 'application/pdf', nullable: true}"
LABEL com.envoyai.info="\
name: Echo Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"