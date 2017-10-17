FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []
LABEL mccoy.schema_in "\
title: 'test-dicom-echo-in'\n\
type: 'object'\n\
properties:\n\
  test-dicom:\n\
    type: array\n\
    items:\n\
      type: string\n\
      format: base64\n\
      title: test.dcm\n\
    _mime-type: application/dcm\n\
    _control: directory"

LABEL mccoy.schema_out "\
title: 'test-dicom-echo-out'\n\
type: 'object'\n\
properties:\n\
  test-dicom:\n\
    type: array\n\
    items:\n\
      type: string\n\
      format: base64\n\
      title: test.dcm\n\
    _mime-type: application/dcm\n\
    _control: directory"

LABEL mccoy.info "\
name: 'Test Dicom Machine'\n\
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