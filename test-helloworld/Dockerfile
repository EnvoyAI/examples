FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2 \

com.envoyai.schema-in="\
hello:\n\
 type: string\n\
 title: hello" \

com.envoyai.schema-out="\
hello:\n\
  type: string\n\
  title: hello" \

com.envoyai.info="\
name: Test Hello World\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: McCoy Medical Technologies\n\
abstract: N/a\n\
date_trained: N/a\n\
data_source: N/a\n\
ground_truth: N/a\n\
algorithm: N/a\n\
performance: N/a\n\
fda_status: N/\n"
