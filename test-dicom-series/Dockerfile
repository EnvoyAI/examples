FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python tree
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
dicom-series-in:\n\
  dicom-type: dicom-series"
LABEL com.envoyai.schema-out="\
dicom-series-out:\n\
  dicom-type: dicom-series"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: input-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: dicom-series-in\n\
results-display-group:\n\
  display-elements:\n\
    - title: Output DICOM\n\
      id: output-dicom\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: dicom-series-out"
LABEL com.envoyai.info="\
name: Test Dicom Series Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"
