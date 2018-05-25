#!/bin/bash
# if needed move input files into place
#cp /envoyai/input/* /root/.wine32/drive_c/data/input/

# Run windows executable
xvfb-run wine HelloWindows.exe

# if needed move output files into place
#cp /root/.wine32/drive_c/data/output/* /envoyai/output/