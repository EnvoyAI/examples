FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python tree
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
image-in.dcm:\n\
  dicom-type: dicom-image"
LABEL com.envoyai.schema-out="\
image-out.dcm:\n\
  dicom-type: dicom-image"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: input-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: image-in.dcm\n\
results-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: output-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: image-out.dcm"
LABEL com.envoyai.info="\
name: Test Dicom Image Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"
