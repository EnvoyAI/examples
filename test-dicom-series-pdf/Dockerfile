FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -U fpdf
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python3","cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
dicom-series-in:\n\
  dicom-type: dicom-series"
LABEL com.envoyai.schema-out="\
out.pdf:\n\
  mime-type: application/pdf"
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
    - title: Output PDF\n\
      id: output-pdf\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: out.pdf"
LABEL com.envoyai.info="\
name: Dicom Series PDF Machine\n\
title: Dicom Series PDF Machine\n\
author: Staff\n\
organization: EnvoyAI"
