FROM nvidia/cuda:9.0-runtime-ubuntu16.04
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["./deviceQuery"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.nvidia=true
LABEL com.envoyai.schema-in="\
name:\n\
 type: string"
LABEL com.envoyai.schema-out="\
hello:\n\
  type: string"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: What is your name?\n\
      id: in_str\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: name\n\
results-display-group:\n\
  display-elements:\n\
    - title: Terminator's response\n\
      id: out_str\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: hello\n\
result-summary:\n\
  content:\n\
    pointer:\n\
      source: output\n\
      property: hello"
LABEL com.envoyai.info="\
name: Cuda Test\n\
title: Test machine for testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
