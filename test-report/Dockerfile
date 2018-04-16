FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python-dicom
ADD . /prog
WORKDIR /prog
RUN chmod a+x annotate.py gsps.py
ENTRYPOINT ["python", "cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
input-image: {dicom-type: dicom-image}\n\
finding: {enum: ['pneumothorax','pneumonia','pulmonary-nodules']}"
LABEL com.envoyai.schema-out="\
pneumothorax-present:\n\
  type: boolean\n\
pneumonia-present:\n\
  type: boolean\n\
pulmonary-nodule-present:\n\
  type: boolean\n\
pulmonary-nodule-volume:\n\
  type: number"
LABEL com.envoyai.report="\
findings:\n\
  - code: 36118008\n\
    code-system: snomed-ct\n\
    present:\n\
      pointer:\n\
        source: output\n\
        property: pneumothorax-present\n\
  - code: 233604007\n\
    code-system: snomed-ct\n\
    present:\n\
      pointer:\n\
        source: output\n\
        property: pneumonia-present\n\
  - code: 445249002\n\
    code-system: snomed-ct\n\
    present:\n\
      pointer:\n\
        source: output\n\
        property: pulmonary-nodule-present\n\
measurements:\n\
  - code: 364639007|Feature of a mass| : 118565006|Volume| = 396162003|mm3|\n\
    code-system: snomed-ct\n\
    value:\n\
      pointer:\n\
        source: output\n\
        property: pulmonary-nodule-volume"
LABEL com.envoyai.info="\
name: Findings Demo\n\
title: Demonstration for returning radiology report findings.\n\
author: Staff\n\
organization: EnvoyAI"
