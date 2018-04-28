FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python-dicom
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python", "cmd.py"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
input-image: { dicom-type: dicom-image }"
LABEL com.envoyai.schema-out="\
pulmonary-nodules:\n\
  type: array\n\
  items:\n\
    type: object\n\
    properties:\n\
      classification: { type: string }\n\
      volume: { type: number }"
LABEL com.envoyai.report="\
findings:\n\
  - code: '364639007|Feature of a mass|'\n\
    code-system: snomed-ct\n\
    value:\n\
      pointer:\n\
        source: output\n\
        property: pulmonary-nodules\n\
        sub-properties:\n\
          classification:\n\
            code: '246200002 | Texture (attribute) |'\n\
          volume:\n\
            code: '118565006|Volume| = 396162003|mm3|'"
LABEL com.envoyai.info="\
name: Findings Demo\n\
title: Demonstration for returning radiology report findings.\n\
author: Staff\n\
organization: EnvoyAI"
