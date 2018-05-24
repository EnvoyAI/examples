FROM ubuntu:16.04
# reccomended to add 32bit arch for wine
RUN dpkg --add-architecture i386
# install things to help install wine
RUN apt-get update \
 && apt-get install -y wget software-properties-common python-software-properties apt-transport-https cabextract telnet xvfb
# register repo and install winehq
RUN wget -nc https://dl.winehq.org/wine-builds/Release.key \
 && apt-key add Release.key \
 && apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ \
 && apt-get update \
 && apt-get install --install-recommends -y winehq-stable

ENV DISPLAY=":0.0"
ENV WINEARCH="win32"
ENV WINEPREFIX="/root/.wine32"

RUN xvfb :0 -screen 0 1024x768x16 \
 & mkdir -p $WINEPREFIX \
 && cd $WINEPREFIX \
 && wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks \
 && chmod +x winetricks \
 && wine wineboot --init \
 && sh ./winetricks d3dx9 corefonts vcrun2015

# copy windows command line exe
ADD HelloWindows/Debug /prog
ADD runWine.sh /prog/runWine.sh
# run it
WORKDIR /prog
#ENTRYPOINT ["/bin/bash","-c","wine \"HelloWindows.exe /nogui\""]
#ENTRYPOINT ["wine","HelloWindows.exe"]
ENTRYPOINT ["/bin/bash","runWine.sh"]
# envoyai metadata
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
