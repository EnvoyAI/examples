FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL com.envoyai.metadata-version=2
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
LABEL com.envoyai.selector="\
selector-type: accept-reject"
LABEL com.envoyai.info="\
name: Hello World\n\
title: Test machine for demonstration or testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
