FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
dicom-study-in:\n\
  dicom-type: dicom-study"
LABEL com.envoyai.schema-out="\
dicom-study-out:\n\
  dicom-type: dicom-study"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: input-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: dicom-study-in\n\
results-display-group:\n\
  display-elements:\n\
    - title: Output DICOM\n\
      id: output-dicom\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: dicom-study-out"
LABEL com.envoyai.info="\
name: Test Dicom Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"
