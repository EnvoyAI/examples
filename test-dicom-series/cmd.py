from subprocess import call
import shutil

call(["tree", "/envoyai/input/dicom-series-in"])
# if no args were passed we read from /envoyai/input and write to /envoyai/output
shutil.copytree('/envoyai/input/dicom-series-in','/envoyai/output/dicom-series-out')
exit(0)
