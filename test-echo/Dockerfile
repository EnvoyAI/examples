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
  test-date: {type: 'string', format: 'date-time', title: 'test-date', _order: 3}\n\
  test.jpg: {type: 'string', format: 'base64', title: 'test.jpg', _mime-type: 'image/jpg', _order: 4, '_control': 'file'}\n\
  test.zip: {type: 'string', format: 'base64', title: 'test.zip', _mime-type: 'application/octet-stream', _order: 5, '_control': 'file'}\n\
  test-enum: {type: 'string', 'enum': ['A', 'B', 'C'], title: 'test-enum', _order: 6}\n\
  test-integer: {type: 'integer', title: 'test-integer', _order: 7}\n\
  test-float: {type: 'number', title: 'test-float', _order: 8}\n\
  test-percentage: {type: 'number', title: 'test-percentage', format: 'percentage', _order: 9}\n\
  test-bool: {type: 'boolean', title: 'test-bool', _order: 10}\n\
  test-img-url: {type: 'string', title: 'test-img-url', _order: 11}\n\
  test-img-url-array:\n\
    type: 'array'\n\
    items:\n\
      type: 'object'\n\
      properties:\n\
        title: {type: 'string', title: 'Title', _order:1}\n\
        image: {type: 'string', title: 'Image', _order:2}\n\
    title: 'test-img-url-array'\n\
    '_order': 12\n\"

LABEL mccoy.schema_out "\
title: 'test_echo'\n\
type: 'object'\n\
properties:\n\
  test-string: {type: 'string', title: 'test-string', _order: 1}\n\
  test-paragraph: {type: 'string', title: 'test-paragraph', format: 'paragraph', _order: 2, _control: 'textarea'}\n\
  test-date: {type: 'string', format: 'date-time', title: 'test-date', _order: 3}\n\
  test.jpg: {type: 'string', format: 'base64', title: 'test.jpg', _mime-type: 'image/jpg', _order: 4, '_control': 'file'}\n\
  test.zip: {type: 'string', format: 'base64', title: 'test.zip', _mime-type: 'application/octet-stream', _order: 5, '_control': 'file'}\n\
  test-enum: {type: 'string', 'enum': ['A', 'B', 'C'], title: 'test-enum', _order: 6}\n\
  test-integer: {type: 'integer', title: 'test-integer', _order: 7}\n\
  test-float: {type: 'number', title: 'test-float', _order: 8}\n\
  test-percentage: {type: 'number', title: 'test-percentage', format: 'percentage', _order: 9}\n\
  test-bool: {type: 'boolean', title: 'test-bool', _order: 10}\n\
  test-img-url: {type: 'string', format: 'imageSrc', title: 'test-img-url', _mime-type: 'image/jpg', _order: 11}\n\
  test-img-url-array:\n\
    type: 'array'\n\
    items:\n\
      type: 'object'\n\
      properties:\n\
        title: {type: 'string', title: 'Title'}\n\
        image: {type: 'string', title: 'Image', format: 'imageSrc', _mime-type: 'image/jpg'}\n\
    title: 'test-img-url-array'\n\
    '_order': 12\n\
    '_control': 'carosel'"

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