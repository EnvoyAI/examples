# EnvoyAI PHI Handling
In order to ensure that no PHI gets sent from the hospital data center to
the EnvoyAI Inference cloud, while still ensuring that Machines get the data
required to perform analysis and inferences, and while ensuring the results
are easily usable by any consumers, the EnvoyAI Liaison has a carefully designed
deidentification and reidentification system.

## De-Identification
EnvoyAI's deidentification model is based on the __"Basic Application Level Confidentiality Profile"__
outlined in Part 15, section E2 of the DICOM standard. We perform deidentification
by building copies of the submitted studies using lists of known safe tags
that we compile for each modality. This protects us from accidentally including
PHI in private tags.  The original studies are never sent outside of the
hospital or practice data center.

We handle dates according to the __"Retain Longitudinal Temporal Information with Modified Dates Option"__
described in section E3. It should also be noted that we allow our development
partners to request exceptions for specific fields that their applications
require. To date, those exceptions have have included gender, equipment
manufacturer, and model name. These exceptions apply only when submitting
data to those specific applications and should be considered when selecting
applications for use.

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

