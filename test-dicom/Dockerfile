FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]

LABEL \
com.envoyai.schema-in="\
test-dicom:\n\
  dicom-type: dicom-study" \
\
com.envoyai.schema-out="\
test-dicom:\n\
  dicom-type: dicom-study" \
\
com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: input-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: test-dicom\n\
results-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: input-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: test-dicom" \
\
com.envoyai.selector="accept-reject"\
\
com.envoyai.info="\
name: Test Dicom Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI\n\
abstract: N/a\n\
date_trained: N/a\n\
data_source: N/a\n\
ground_truth: N/a\n\
algorithm: N/a\n\
performance: N/a\n\
fda_status: N/a\n\
links: N/a"
