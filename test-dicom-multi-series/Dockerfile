FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python tree
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
dicom-series-in-1:\n\
  dicom-type: dicom-series\n\
dicom-series-in-2:\n\
  dicom-type: dicom-series"
LABEL com.envoyai.schema-out="\
dicom-series-out-a:\n\
  dicom-type: dicom-series\n\
dicom-series-out-b:\n\
  dicom-type: dicom-series"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input DICOM 1\n\
      id: input-dicom-1\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: dicom-series-in-1\n\
    - title: Input DICOM 2\n\
      id: input-dicom-2\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: dicom-series-in-2\n\
results-display-group:\n\
  display-elements:\n\
    - title: Output DICOM a\n\
      id: output-dicom-a\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: dicom-series-out-a\n\
    - title: Output DICOM b\n\
      id: output-dicom-b\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: dicom-series-out-b"
LABEL com.envoyai.info="\
name: Dicom Multi Series Machine\n\
title: Dicom Multi Series Machine\n\
author: Staff\n\
organization: EnvoyAI"
