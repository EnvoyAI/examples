FROM ubuntu:16.04
RUN apt-get update && apt-get install -y iputils-ping
ENTRYPOINT ["/bin/ping","-c","3","google.com"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.network=true
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
    - title: Ping Response\n\
      id: out_str\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: result"
LABEL com.envoyai.info="\
name: Network Test\n\
title: Test machine for testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
