from subprocess import call
import shutil

# if no args were passed we read from /envoyai/input and write to /envoyai/output

call(["tree", "/envoyai/input/dicom-series-in-1"])
shutil.copytree('/envoyai/input/dicom-series-in-1','/envoyai/output/dicom-series-out-a')

call(["tree", "/envoyai/input/dicom-series-in-2"])
shutil.copytree('/envoyai/input/dicom-series-in-2','/envoyai/output/dicom-series-out-b')

exit(0)
