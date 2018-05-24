FROM suchja/wine:dev
ADD HelloWindows/Debug/HelloWindows.exe /prog/HelloWindows.exe
WORKDIR /prog
ENTRYPOINT ["wine","HelloWindows.exe"]
LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.schema-in="\
name:\n\
 type: string"
LABEL com.envoyai.schema-out="\
hello:\n\
  type: string"
LABEL com.envoyai.info="\
name: Hello World\n\
title: Test machine for demonstration or testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
