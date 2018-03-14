FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python3 python3-pip tree
RUN pip3 install -U numpy pydicom==1.0.1rc1
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python3","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
in.dcm:\n\
  dicom-type: dicom-image"
LABEL com.envoyai.schema-out="\
out.dcm:\n\
  dicom-type: dicom-image"
LABEL com.envoyai.info="\
name: Test Dicom Image Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"
