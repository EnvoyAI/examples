import os

# ignore chest xray, because this is just a demo
#with open("/envoyai/input/in.dcm", "r") as f:

# load input parameter
with open("/envoyai/input/finding", "r") as f:
    finding = f.read()

# write output
with open('/envoyai/output/pneumothorax-present', 'w') as f:
    f.write(str(finding == "pneumothorax"))
with open('/envoyai/output/pneumonia-present', 'w') as f:
    f.write(str(finding == "pneumonia"))
with open('/envoyai/output/pulmonary-nodule-present', 'w') as f:
    f.write(str(finding == "pulmonary-nodules"))

if finding == "pulmonary-nodules":
    with open('/envoyai/output/pulmonary-nodule-volume', 'w') as f:
        f.write(str(22.8))
