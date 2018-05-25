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

# setup vars for wine
ENV DISPLAY=":0.0"
ENV WINEARCH="win32"
ENV WINEPREFIX="/root/.wine32"
ENV WINESYSTEM32="/root/.wine32/drive_c/windows/system32"
ENV WINEDLLOVERRIDES="mscoree,mshtml="

# pull down winetricks, and install requirements
# vcrun2015 and vcrun2010 are Visual Studio C++ Redistributables
RUN set -e \
 && mkdir -p $WINEPREFIX \
 && cd $WINEPREFIX \
 && wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks \
 && chmod +x winetricks \
 && xvfb-run wine wineboot --init \
 && xvfb-run wineserver -w \
 && xvfb-run sh ./winetricks -q d3dx9 corefonts vcrun2015 vcrun2010

# copy windows command line exe
ADD HelloWindows/Release /prog
ADD runWine.sh /prog/runWine.sh
# run it in a simple bash script.
WORKDIR /prog
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
name: Hello Wine\n\
title: Test machine for demonstration or testing purposes only.\n\
author: Staff\n\
organization: EnvoyAI"
