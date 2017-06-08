FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install python-dateutil
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []
LABEL mccoy.schema_in "\
title: 'test_echo'\n\
type: 'object'\n\
properties:\n\
  test-string: {type: 'string', title: 'test-string', _order: 1}\n\
  test-paragraph: {type: 'string', title: 'test-paragraph', format: 'paragraph', _order: 2, '_control': 'textarea'}\n\
  test-enum: {type: 'string', 'enum': ['A', 'B', 'C'], title: 'test-enum', _order: 3}\n\
  test-date: {type: 'string', format: 'date-time', title: 'test-date', _order: 4}\n\
  test-bool: {type: 'boolean', title: 'test-bool', _order: 5}\n\
  test.zip: {type: 'string', format: 'base64', title: 'test.zip', _mime-type: 'application/octet-stream', _order: 6, '_control': 'file'}\n\
  test.jpg: {type: 'string', format: 'base64', title: 'test.jpg', _mime-type: 'image/jpg', _order: 7, '_control': 'file'}\n\
  test-object:\n\
    type: 'object'\n\
    properties:\n\
      test-integer: {type: 'integer', title: 'test-integer', _order: 1}\n\
      test-float: {type: 'number', title: 'test-float', _order: 2}\n\
      test-percentage: {type: 'number', title: 'test-percentage', format: 'percentage', _order: 3}\n\
    title: 'test-object'\n\
    '_order': 8\n\
  test-img-url-array:\n\
    type: 'array'\n\
    items:\n\
      title: 'img-url-record'\n\
      type: 'object'\n\
      properties:\n\
        title: {type: 'string', title: 'Title', _order:1}\n\
        image: {type: 'string', title: 'Image', _order:2}\n\
    title: 'test-img-url-array'\n\
    '_order': 9\n\
  test-keywords-array:\n\
    type: 'array'\n\
    items:\n\
      title: 'keyword'\n\
      type: 'string'\n\
    title: 'test-keywords-array'\n\
    '_order': 10\n\
  test-file-array:\n\
    type: 'array'\n\
    items:\n\
      type: 'string'\n\
      format: 'base64'\n\
      '_mime-type': 'application/octet-stream'\n\
      title: 'download.jpg'\n\
    title: 'test-file-array'\n\
    '_order': 11\n\
    '_control': 'directory'"

LABEL mccoy.schema_out "\
title: 'test_echo'\n\
type: 'object'\n\
properties:\n\
  test-string: {type: 'string', title: 'test-string', _order: 1}\n\
  test-paragraph: {type: 'string', title: 'test-paragraph', format: 'paragraph', _order: 2, '_control': 'textarea'}\n\
  test-enum: {type: 'string', 'enum': ['A', 'B', 'C'], title: 'test-enum', _order: 3}\n\
  test-date: {type: 'string', format: 'date-time', title: 'test-date', _order: 4}\n\
  test-bool: {type: 'boolean', title: 'test-bool', _order: 5}\n\
  test.zip: {type: 'string', format: 'base64', title: 'test.zip', _mime-type: 'application/octet-stream', _order: 6, '_control': 'file'}\n\
  test.jpg: {type: 'string', format: 'base64', title: 'test.jpg', _mime-type: 'image/jpg', _order: 7, '_control': 'file'}\n\
  test-object:\n\
    type: 'object'\n\
    properties:\n\
      test-integer: {type: 'integer', title: 'test-integer', _order: 1}\n\
      test-float: {type: 'number', title: 'test-float', _order: 2}\n\
      test-percentage: {type: 'number', title: 'test-percentage', format: 'percentage', _order: 3}\n\
    title: 'test-object'\n\
    '_order': 8\n\
  test-img-url-array:\n\
    type: 'array'\n\
    items:\n\
      title: 'img-url-record'\n\
      type: 'object'\n\
      properties:\n\
        title: {type: 'string', title: 'Title'}\n\
        image: {type: 'string', title: 'Image', format: 'imageSrc', _mime-type: 'image/jpg'}\n\
    title: 'test-img-url-array'\n\
    '_order': 9\n\
    '_control': 'carousel'\n\
  test-keywords-array:\n\
    type: 'array'\n\
    items:\n\
      title: 'str'\n\
      type: 'string'\n\
    title: 'test-keywords-array'\n\
    '_order': 10\n\
  test-file-array:\n\
    type: 'array'\n\
    items:\n\
      type: 'string'\n\
      format: 'base64'\n\
      '_mime-type': 'application/octet-stream'\n\
      title: 'download.jpg'\n\
    title: 'test-file-array'\n\
    '_order': 11"

LABEL mccoy.info "\
name: 'Test Echo Machine'\n\
title: 'Test machine for demonstration or testing purposes only'\n\
author: 'Staff'\n\
organization: 'McCoy Medical Technologies'\n\
abstract: 'N/a'\n\
date_trained: 'N/a'\n\
data_source: 'N/a'\n\
ground_truth: 'N/a'\n\
algorithm: 'N/a'\n\
performance: 'N/a'\n\
fda_status: 'N/a'\n\
links: 'N/a'"