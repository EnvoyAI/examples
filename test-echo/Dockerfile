FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install python-dateutil
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.nvidia=true \
    com.envoyai.schema-in="\
test-string: {type: 'string', title: 'test-string'}\n\
test-paragraph: {type: 'string', title: 'test-paragraph'}\n\
test-enum: {'enum': ['A', 'B', 'C'], title: 'test-enum'}\n\
test-date: {type: 'date-time', title: 'test-date'}\n\
test-bool: {type: 'boolean', title: 'test-bool'}\n\
test.zip: {title: 'test.zip', mime-type: 'application/octet-stream'}\n\
test.jpg: {title: 'test.jpg', mime-type: 'image/jpg'}\n\
test.dcm: {title: 'test.dcm', mime-type: 'image/dcm'}\n\
test-object:\n\
  type: 'object'\n\
  properties:\n\
    test-integer: {type: 'integer', title: 'test-integer'}\n\
    test-float: {type: 'number', title: 'test-float'}\n\
    test-percentage: {type: 'number', title: 'test-percentage', format: 'percentage'}\n\
    title: 'test-object'\n\
test-img-url-array:\n\
  title: 'test-img-url-array'\n\
  type: 'array'\n\
  items:\n\
    title: 'img-url-record'\n\
    type: 'object'\n\
    properties:\n\
      title: {type: 'string', title: 'Title'}\n\
      image: {type: 'string', title: 'Image'}\n\
test-keywords-array:\n\
  title: 'test-keywords-array'\n\
  type: 'array'\n\
  items:\n\
    title: 'keyword'\n\
    type: 'string'\n\
test-file-array:\n\
  title: 'test-file-array'\n\
  type: 'array'\n\
  items:\n\
    mime-type: application/octet-stream\n\
    title: 'download.jpg'" \
    com.envoyai.schema-out="\
test-string: {type: 'string', title: 'test-string'}\n\
test-paragraph: {type: 'string', title: 'test-paragraph'}\n\
test-enum: {'enum': ['A', 'B', 'C'], title: 'test-enum'}\n\
test-date: {type: 'date-time', title: 'test-date'}\n\
test-bool: {type: 'boolean', title: 'test-bool'}\n\
test.zip: {title: 'test.zip', mime-type: 'application/octet-stream'}\n\
test.jpg: {title: 'test.jpg', mime-type: 'image/jpg'}\n\
test.dcm: {title: 'test.dcm', mime-type: 'image/dcm'}\n\
test-object:\n\
  type: 'object'\n\
  properties:\n\
    test-integer: {type: 'integer', title: 'test-integer'}\n\
    test-float: {type: 'number', title: 'test-float'}\n\
    test-percentage: {type: 'number', title: 'test-percentage', format: 'percentage'}\n\
    title: 'test-object'\n\
test-img-url-array:\n\
  title: 'test-img-url-array'\n\
  type: 'array'\n\
  items:\n\
    title: 'img-url-record'\n\
    type: 'object'\n\
    properties:\n\
      title: {type: 'string', title: 'Title'}\n\
      image: {type: 'string', title: 'Image'}\n\
test-keywords-array:\n\
  title: 'test-keywords-array'\n\
  type: 'array'\n\
  items:\n\
    title: 'keyword'\n\
    type: 'string'\n\
test-file-array:\n\
  title: 'test-file-array'\n\
  type: 'array'\n\
  items:\n\
    mime-type: application/octet-stream\n\
    title: 'download.jpg'" \
    com.envoyai.info="\
name: 'Test Echo Machine'\n\
title: 'Test machine for demonstration or testing purposes only'\n\
author: 'Staff'\n\
organization: 'EnvoyAI'\n\
abstract: 'N/a'\n\
date_trained: 'N/a'\n\
data_source: 'N/a'\n\
ground_truth: 'N/a'\n\
algorithm: 'N/a'\n\
performance: 'N/a'\n\
fda_status: 'N/a'\n\
links: 'N/a'"