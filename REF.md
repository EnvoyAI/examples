# EnvoyAI Machine API - LABEL Reference
Here you will find an explanation for every metadata LABEL that can be provided
in the Machine's Dockerfile, along with reference tables and an example.

## Required LABELs
### com.envoyai.metadata-version
Docker LABEL interface version - version 1 is deprecated, so value must be version 2
```Dockerfile
LABEL com.envoyai.metadata-version=2
```
### com.envoyai.schema-in
Formal description of the inputs to the Machine. The EnvoyAI Platform uses
a system based on JSON-Schema but uses different defaults, and has additional
features to describe files and DICOM studies. Either JSON or YAML formatted
schemas are accepted.

```Dockerfile
LABEL com.envoyai.schema-in="\
dicom-study-in:\n\
  dicom-type: dicom-study"
```
See the [hello world walkthrough](#/test-hello/README.md/#2-schemas) for more info.
### com.envoyai.schema-out
Formal description of the outputs of the Machine. The EnvoyAI Platform uses
a system based on JSON-Schema but uses different defaults, and has additional
features to describe files and DICOM studies. Either JSON or YAML formatted
schemas are accepted.

```Dockerfile
LABEL com.envoyai.schema-out="\
dicom-study-out:\n\
  dicom-type: dicom-study"
```
See the [hello world walkthrough](#/test-hello/README.md/#2-schemas) for more info.
### com.envoyai.info
Information about the machine, author, and organization. This information is currently
only visible on the developer portal, but after some modification to the available properties
and some curation of the values, this may be visible publicly.
Here is a list of properties that may be provided, along with examples from an imaginary company, AlgoHoldings.

|Name                |Key               |Example                                                                                              |Description|
|--------------------|------------------|-----------------------------------------------------------------------------------------------------|-----------|
|Name *              |name              |"AlgoEye &trade;"                                                                                    |The Name of your Machine|
|Title               |title             |"Neural Net powered detector of incidental findings."                                                |Title (treated as a sub-title) of your Machine|
|Author              |author            |"Dr. John Doe PHD" OR "AlgoHoldings Staff"                                                           |Individual(s) credited with authorship|
|Organization        |organization      |AlgoHoldings &copy;                                                                                  |Company or Organization with ownership|
|Input Details       |input-details     |"Chest CR" OR "Screening Chest CT with 3mm slices"                                                   |Description of the input of an algorithm, this usually needed, beyond the constraints set in schema-in, to properly demonstrate the Machine.|
|Output Details      |output-details    |"Secondary Capture with RGB Overlay" OR "incidental findings and measurements"                       |Description of the output of an algorithm, this helps interested parties to understand the outputs and how they might be used.|
|Link to Manual      |link-to-manual    |"https://algoholdings.ai/docs/algoeye.pdf"                                                           |URL to the user manual.|
|Link to Samples     |link-to-samples   |"https://s3.amazonaws.com/algo-eye-samples/sample1.zip"                                              |URL to sample input and or output data.|
|Release Version     |release-version   |"1.0.1-2017-01-02#78b23445" OR "2.0.0-RC1"                                                           |Version of underlying Algorithm, not the Machine, required for regulatory purposes.|
|Abstract            |abstract          |"Bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla"|A summary of the the underlying algorithm, and how the Machine should be used.|
|Fda Status          |fda-status        |"Pending" OR "FDA Cleared" OR "Research Only"                                                        |United States Regulatory Status|
|CE Mark Status      |ce-mark-status    |"Pending" OR "CE Mark Cleared" OR "Research Only"                                                    |European Union Regulatory Status|
|Health Canada Status|health-ca-status  |"Pending" OR "Health Canada Cleared" OR "Research Only"                                              |Canada Regulatory Status|
|PMDA Status         |pmda-status       |"Pending" OR "PMDA Cleared" OR "Research Only"                                                       |Japan Regulatory Status|
|MFDS status         |mfds-status       |"Pending" OR "MFDS Cleared" OR "Research Only"                                                       |Korea Regulatory Status|
|Date Trained        |date-trained      |"2017-01-02"                                                                                         |Date that the Machine Learning Model, if used, was trained.|
|Data Source         |data-source       |"University of Imagination Hospital Chest CR repository"                                             |Source of the training data, if used.|
|Ground Truth        |ground-truth      |"Chest CR annotated by board certified radiologists"                                                 |Description of the method by which training data, if used, was labeled.|
|Training Algorithm  |training-algorithm|"Neural Net" or "Statistical Regressions after feature extraction with heuristics based segmentation"|Description of the algorithms used.|
|Performance         |performance       |"99.98% Accuracy"                                                                                    |Accuracy and or precision, and any other relevant measurements of performance.|
\* Only Name is required.<br />
*Note: the data type of all values is `string`*
```Dockerfile
LABEL com.envoyai.info="\
name: Echo Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"
```
## Optional Runtime Parameter LABELs
### com.envoyai.nvidia
default is `false`. If present and `true`, then the Docker execution
environment will be nvidia-docker, allowing access to NVidia GPU.
```Dockerfile
LABEL com.envoyai.nvidia=true
```
See [test-cuda](#/test-cuda) for a simplified example.<br />
See [related faq](./FAQ.md#does-envoyai-support-cuda) for more information.
### com.envoyai.network
default is `false`. If present and `true`, then the Docker execution
environment will have access to the internet.
```Dockerfile
LABEL com.envoyai.network=true
```
This does have implications for use in production use, see
[related faq](./FAQ.md/#can-my-machine-access-the-internet) for more information.
### com.envoyai.timeout
The number of minutes the Docker should be awaited before exiting. Default is `60`.
### com.envoyai.dicom-tags
Any dicom tags in addition to the minimum set of fields for a given SOP.
each tag should be referenced by it's _keyword_ and separated on a new line.
```Dockerfile
LABEL com.envoyai.network="\
PatientSex\
PatientAge"
```
We have found [dicom.innolitics.com](https://dicom.innolitics.com/) to be
a good dicom tag (and _keyword_) reference.
For more information about deidentifacation and reidentifacation of dicom
see [PHI.md](./FAQ.md).

## Optional Informational Parameter LABELs
### com.envoyai.display
This should have a value if the Machine's results can be viewed using a
radiology viewer. If missing, a default value will be created.

`com.envoyai.display` must contain two ordered lists of _display-elements_, `source-display-group` generally
representing the inputs, and `results-display-group` generally representing the outputs, as well as a `result-summary`
which provides the consumer with a

Each _display-element_ must have a title, id, and content. Title simply suggests how the viewer should label the value,
the id allows you to reference the display element in feedback, the content tells the viewer what to actually show,
usually with a _pointer_ object. A _pointer_ object contains a single property, `pointer`, which in turn has a `source` prop
describing if the value comes from the input or the output of the algorithm, and a `property` prop which will match the name
of the property from either input or output.

```Dockerfile
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: input-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: dicom-study-in\n\
results-display-group:\n\
  display-elements:\n\
    - title: Input DICOM\n\
      id: output-dicom\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: dicom-study-out"
```
### com.envoyai.selector
This should have a value if a Machine's results can be viewed using a
radiology viewer. If missing, a default value will be created.
The current feedback selectors:

|Name           |Key                         |LABEL value|Description|
|---------------|----------------------------|-----------|-----------|
|Accept / Reject|`accept-reject`             |`selector-type: accept-reject`| will prompt the user to either agree or disagree with the results.
|Choose One     |`choose-one-display-element`|`selector-type: choose-one-display-element`<br />`selector-config:`<br />&nbsp;&nbsp;`  choose-options:`<br />&nbsp;&nbsp;&nbsp;&nbsp;`- display-element-id-1`<br />&nbsp;&nbsp;&nbsp;&nbsp;`- display-element-id-2`<br />&nbsp;&nbsp;&nbsp;&nbsp;`- display-element-id-3`| will prompt the user to either agree or disagree with the results.

```Dockerfile
LABEL com.envoyai.selector="\
selector-type: choose-one-display-element\n\
selector-config:\n\
  choose-options:\n\
    - guess-0\n\
    - guess-1\n\
    - guess-2\n\
  default-option: guess-0"
```