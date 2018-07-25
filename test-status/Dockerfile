FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.timeout=1
LABEL com.envoyai.schema-in="\
name:\n\
  type: string\n\
behavior:\n\
  enum: [ error, run, timeout ]"
LABEL com.envoyai.schema-out="\
hello:\n\
  type: string"
LABEL com.envoyai.info="\
name: Test Status\n\
title: Test machine for demonstration or testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
