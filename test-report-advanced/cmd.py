import os

# ignore chest xray, because this is just a demo
# with open("/envoyai/input/in.dcm", "r") as f:

# load input parameter
import random

# write output
os.mkdir('/envoyai/output/pulmonary-nodules')
os.mkdir('/envoyai/output/pulmonary-nodules/0')
with open('/envoyai/output/pulmonary-nodules/0/volume', 'w') as f:
    f.write(str(22.8))
with open('/envoyai/output/pulmonary-nodules/0/classification', 'w') as f:
    f.write("part-solid")
os.mkdir('/envoyai/output/pulmonary-nodules/1')
with open('/envoyai/output/pulmonary-nodules/1/volume', 'w') as f:
    f.write(str(12.2))
with open('/envoyai/output/pulmonary-nodules/1/classification', 'w') as f:
    f.write("nonsolid")

