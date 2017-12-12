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
test-object:\n\
  type: 'object'\n\
  properties:\n\
    test-string: {type: 'string'}\n\
    test-percentage: {type: 'percentage'}\n\
test-keywords-array:\n\
  type: 'array'\n\
  items:\n\
    title: 'keyword'\n\
    type: 'string'\n\
test-object-array:\n\
  type: 'array'\n\
  items:\n\
    title: 'test-object'\n\
    type: 'object'\n\
    properties:\n\
      test-string: {type: 'string'}\n\
      test-percentage: {type: 'percentage'}\n\
test-file-array:\n\
  type: 'array'\n\
  items:\n\
    mime-type: application/octet-stream"
LABEL com.envoyai.schema-out="\
test-object:\n\
 type: 'object'\n\
 properties:\n\
   test-string: {type: 'string'}\n\
   test-percentage: {type: 'percentage'}\n\
test-keywords-array:\n\
 type: 'array'\n\
 items:\n\
   title: 'keyword'\n\
   type: 'string'\n\
test-object-array:\n\
 type: 'array'\n\
 items:\n\
   title: 'test-object'\n\
   type: 'object'\n\
   properties:\n\
     test-string: {type: 'string'}\n\
     test-percentage: {type: 'percentage'}\n\
test-file-array:\n\
 type: 'array'\n\
 items:\n\
   mime-type: application/octet-stream"
LABEL com.envoyai.info="\
name: Echo Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"