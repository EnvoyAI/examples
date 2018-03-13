FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python-dicom
ADD . /prog
WORKDIR /prog
RUN chmod a+x annotate.py gsps.py
ENTRYPOINT ["python", "annotate.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
input-image:\n\
  dicom-type: dicom-image\n\
text-annotation:\n\
  {type: 'string'}\n\
label-alignment:\n\
  {'enum': ['Left','Right']}"
LABEL com.envoyai.schema-out="\
annotated-series:\n\
  dicom-type: dicom-series"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input Image\n\
      id: input-image\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: input-image\n\
    - title: Text Annotation\n\
      id: text-annotation\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: text-annotation\n\
    - title: Text Alignment\n\
      id: label-alignment\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: label-alignment\n\
results-display-group:\n\
  display-elements:\n\
    - title: Annotated Series\n\
      id: annotated-series\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: annotated-series"
LABEL com.envoyai.selector="\
selector-type: accept-reject"
LABEL com.envoyai.info="\
name: Annotation Demo\n\
title: Adds a GSPS annotation file to an image to create a series \n\
author: Staff\n\
organization: EnvoyAI"
