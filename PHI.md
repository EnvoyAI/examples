# EnvoyAI PHI Handling
In order to ensure that no PHI gets sent from the hospital data center to
the EnvoyAI Inference cloud, while still ensuring that Machines get the data
required to perform analysis and inferences, and while ensuring the results
are easily usable by any consumers, the EnvoyAI Liaison has a carefully designed
deidentification and reidentification system.

## De-Identification
EnvoyAI strips most tags from DICOM instances. We anonymize and include a minimal 
subset of fields that are specific to the modality of the study. Those tags are 
listed below.  Machine developers can specify additional tags that are required 
for their algorithms by attaching special labels to their docker images.

A note on dates: EnvoyAI anonymizes dates by time-shifting them. A random number 
of days is determined for each inference submission and all of the dates in that 
submission are shifted by that number of days. This obscures the dates, but 
preserves the time ranges in your input.

## Re-Identification

Two things happen during re-identification: 
1. Patient data and Study data are copied verbatim from the original studies onto 
the results. A complete list of those fields can be found below.
2. UIDs are remapped so that the results are correctly associated with the original 
study. This includes rewriting GSPS references.



## Details
### Patient and Study Data Applied During Re-Identification
These tags will be reapplied to any new series created by a Machine if they were present on the source study.

|DICOM Tag Keywords|
|------------|
|PatientName|
|PatientID|
|PatientSex|
|...|

### Default Tags for MRI DICOM Instances
These tags will be present on any MR instances passed to your Machine.

|DICOM Tag Keywords|
|------------|
|PatientName|
|PatientID|
|PatientSex|
|...|

### Default Tags for CT DICOM Instances
These tags will be present on any CT instances passed to your Machine.

|DICOM Tag Keywords|
|------------|
|PatientName|
|PatientID|
|PatientSex|
|...|

