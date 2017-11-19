FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.schema-in="\
err:\n\
  title: err\n\
  enum: [timeout, invalid_output, uncaught_exception, exit_code, large_output ]" \
    com.envoyai.schema-out="{ \
out:\n\
  title: out\n\
  type: integer"\
    com.envoyai.info="\
name: Test Err Machine\n\
title: Test machine for demonstration or error handling purposes only\n\
author: Staff\n\
organization: McCoy Medical Technologies\n\
abstract: N/a\n\
date_trained: N/a\n\
data_source: N/a\n\
ground_truth: N/a\n\
algorithm: N/a\n\
performance: N/a\n\
fda_status: N/"
