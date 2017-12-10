FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
LABEL \
com.envoyai.metadata-version=2 \
\
com.envoyai.schema-in="\
hello:\n\
 type: string\n\
 title: hello" \
\
com.envoyai.schema-out="\
hello:\n\
  type: string\n\
  title: hello" \
\
com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: User Input String\n\
      id: in_str\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: hello\n\
result-display-group:\n\
  display-elements:\n\
    - title: Machine Output String\n\
      id: out_str\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: hello\n\
result-summary:\n\
  content:\n\
    pointer:\n\
      source: output\n\
      property: hello"\
\
com.envoyai.selector="\
selector-type: accept-reject"\
\
com.envoyai.info="\
name: Hello World\n\
title: Test machine for demonstration or testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
