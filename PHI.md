# EnvoyAI PHI Handling
In order to ensure that no PHI gets sent from the hospital data center to
the EnvoyAI Inference cloud, while still ensuring that Machines get the data
required to perform analysis and inferences, and while ensuring the results
are easily usable by any consumers, the EnvoyAI Liaison has a carefully designed
deidentification and reidentification system.
## Deidentification
Documentation in progress...

Only required data is sent to the cloud.
Each SOP Class has a different set of required fields.
In addition any additional Dicom Tags that a Machine specifies will be copied into the new instance.
## Reidentification
Documentation in progress...
### Patient and Study data
This table describes all of the dicom tags that will be reapplied to any
new series created by a Machine

|Dicom Tag Keywords|
|------------|
|PatientName|
|PatientID|
|PatientSex|
|...|

*Maybe we should just describe that we copy every Patient, Clinical Trial Subject, General Study, Clinical Trial Study Tag?*
### Series and Instance data
All series and instance data will be *reidentified*, replacing any placeholder
values that were sent to the cloud with the real values that were stored
in the hospital datacenter.