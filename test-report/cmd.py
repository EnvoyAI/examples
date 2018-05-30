import os

# ignore chest xray, because this is just a demo
# with open("/envoyai/input/in.dcm", "r") as f:

# load input parameter
import random

with open("/envoyai/input/finding", "r") as f:
    finding = f.read()

# write output
if finding == "pneumothorax":
    with open('/envoyai/output/pneumothorax', 'w') as f:
        f.write('248702003 | Clicking pneumothorax (disorder) |')
with open('/envoyai/output/pneumonia-present', 'w') as f:
    f.write(str(finding == "pneumonia"))
