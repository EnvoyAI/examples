FROM nvidia/cuda:9.0-runtime-ubuntu16.04
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["./deviceQuery","|","grep","Result",">","/envoyai/output/result"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.nvidia=true
LABEL com.envoyai.schema-in="\
test:\n\
 type: boolean"
LABEL com.envoyai.schema-out="\
result:\n\
  type: string"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements: []\n\
results-display-group:\n\
  display-elements:\n\
    - title: Device Query Response\n\
      id: out_str\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: result"
LABEL com.envoyai.info="\
name: Cuda Test 9.0\n\
title: Test machine for testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
