#!/bin/bash
#Xvfb :0 -screen 0 1024x768x16 &
#DISPLAY=:0.0 wine HelloWindows.exe
xvfb :0 -screen 0 1024x768x16
wine HelloWindows.exe /nogui