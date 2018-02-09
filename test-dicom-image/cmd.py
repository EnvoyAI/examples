from subprocess import call
import shutil

# if no args were passed we read from /envoyai/input and write to /envoyai/output
shutil.copyfile('/envoyai/input/image-in.dcm','/envoyai/output/image-out.dcm')
exit(0)
