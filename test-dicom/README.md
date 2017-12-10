# Dicom Examples

The EnvoyAI Platform has special support for DICOM Studies, Series, and Instances

## Dicom Study
For input properties with `dicom-type: dicom-study`,
each individual SOPInstance will be in a separate file,
named by SOPInstanceID, and organized into subdirectories named
by SeriesInstanceID. This is intended to make it easier to work with,
but is not required for dicom study output. For output properties
with `dicom-type: dicom-study`, one must simply put each SopInstanceId
in a different file, with any name or subdirectory, into the directory
with the appropriate property name.

## Dicom Series
For input properties with `dicom-type: dicom-series`,
each individual SOPInstance will be in a separate file, in the directory
named for the property. For output properties with
`dicom-type: dicom-series`, each SOPInstance must be in a separate file,
with any name, so long as it is under the directory with the appropriate
property name.

## Dicom Image
One can work with Input/Output properties with `dicom-type: dicom-image`
just as they would any other single file type.


## Constraining Properties
You may choose to constrain your input our output in a few ways,
this may make reading input easier, and may improve performance.

|Property                |Example                      |Study|Series|Image|Description|
|------------------------|-----------------------------|-----|------|-----|-----------|
|TransferSyntaxUID       |['1.2.840.10008.1.2']        |✓    |✓     |✓    |Related to `(0002,0010)`, the EnvoyAI Platform will convert the DICOM Study to the specified transfer syntax before providing it to your Machine, when found in an output property, your Machine will be expected to only output DICOM data with the specified syntax.|
|Series-Related-Instances|1                            |     |✓     |     |Similar to Dicom Query Attribute `(0020,1209)`, the number of instances expected in the series.|
|Study-Related-Series    |[1]                          |✓    |      |     |Inspired by `(0020,1206)` and `(0020,1209)`, this is a list, with one entry per series, containing the number of instances in that series.|
|Study-Related-Instances |1                            |✓    |      |     |Inspired by `(0020,1206)` and `(0020,1209)`, this is a list, with one entry per series, containing the number of instances in that series.|
|SOP-Classes             |['1.2.840.10008.5.1.4.1.1.1']|✓    |✓     |✓    |Similar to `(0008,0062)`, a list of all SOP Classes contained in the study.|
|Modalities              |['CR']                       |✓    |✓     |✓    |Similar to `(0008,0061)`, a list of all Modalities contained in the study.|


## Descriptive Properties
You may choose to describe the study in various ways to help describe,
but these won't be used in any automated or programmatic way.
|Property                |Example                      |Study|Series|Image|Description|
|------------------------|-----------------------------|-----|------|-----|-----------|
|StudyDescription        |upper extremities            |✓    |✓     |✓    |An example value that may appear in `(0008,1030)`|
|SeriesDescription       |hand AP                      |     |✓     |✓    |An example value that may appear in `(0008,103e)`|
|SeriesDescriptions      |['hand AP']                  |✓    |      |     |An example value, per series that may appear in `(0008,103e)`|