# Reporting Integration Example
*Note: This is currently a proof of concept, therefore it has not been fully implemented, and may change significantly.*

### Why use the Reporting Interface
The EnvoyAI Reporting Integration will eventually be an extremely powerful
tool in the hands of developers and radiologist. Developers will be able
to write Machines that output the presence of *Findings* or output quantitative
*Measurements*. EnvoyAI will be able to send the Findings and Measurements
to the radiology reporting system, which will beable to enhanse the radiology
workflow in a number of ways:

* Automatically Copying Measurements into a report.
* Automatically checking to make sure a clincal finding was reported,
and warning the radiologist if it is missing.

### How to use the Findings Reporting Interface
The EnvoyAI Findings Reporting Interface is designed to be easy to use.
* Declare a boolean property(s) in your `com.envoyai.schema-out`, this will
represent if the finding exists in the given input.
* Set a value to the property(s) with the Machine's executable (by writing the string "true" or "false" to a
file with the properties name in /envoyai/output).
* Create a `com.envoyai.report` LABEL in your dockerfile
* Set the value of the LABEL to a JSON or YAML object with a `findings`
property.
* For each findings property you have declared, add an object that consists of three parts:
    * A `code` string, representing a code in the referenced coding system
    which represents the finding you wish to communicate.
    * A `code-system` string, representing a coding system (for example snomed-ct)
    * A `pointer` object, referencing the findings boolean property.
    ```Dockerfile
    LABEL com.envoyai.report="\
    findings:\n\
      - code: 36118008\n\
        code-system: snomed-ct\n\
        present:\n\
          pointer:\n\
            source: output\n\
            property: pneumothorax-present\n\
      - code: 233604007\n\
        code-system: snomed-ct\n\
        present:\n\
          pointer:\n\
            source: output\n\
            property: pneumonia-present\n\
      - code: 445249002\n\
        code-system: snomed-ct\n\
        present:\n\
          pointer:\n\
            source: output\n\
            property: pulmonary-nodule-present\n\
    measurements:\n\
      - code: 364639007|Feature of a mass| : 118565006|Volume| = 396162003|mm3|\n\
        code-system: snomed-ct\n\
        value:\n\
          pointer:\n\
            source: output\n\
            property: pulmonary-nodule-volume"
    ```
### Hhow to use the Measurements Reporting Integration
The EnvoyAI Measurement Reporting Integration is just a little more complicated
then the Findings Interface.
* Declare a float property (`{type: 'number'}`) to represent your measurement.
* For each measurement property you have declared, add an object that consists
of the same three parts: `code`, `code-system`, and `pointer`
    * Note that `code` must now include a more specific expression to include
    what is being measured, the measurement type, and the unit. Thankfully
    snomed-ct has this flexibility so we can use the code expression:
    ```snomed-ct
    364639007|Feature of a mass| : 118565006|Volume| = 396162003|mm3|
    ```