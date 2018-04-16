FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python-dicom
ADD . /prog
WORKDIR /prog
RUN chmod a+x annotate.py gsps.py
ENTRYPOINT ["python", "annotate.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
input-image: {dicom-type: dicom-image}\n\
text-annotation: {type: string}\n\
label-alignment: {enum: ['Left','Right']}\n\
circle-radius: {type: integer}\n\
circle-pos-x: {type: integer}\n\
circle-pos-y: {type: integer}"
LABEL com.envoyai.schema-out="\
annotated-series:\n\
  dicom-type: dicom-series"
LABEL com.envoyai.info="\
name: Annotation Demo\n\
title: Adds a GSPS text and circle annotations to an image to create a series \n\
author: Staff\n\
organization: EnvoyAI"
