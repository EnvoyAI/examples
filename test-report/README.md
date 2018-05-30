# Reporting Integration Example
*Note: This is currently a proof of concept, therefore it has not been fully implemented, and may change significantly.*

### Why use the Reporting Interface
The EnvoyAI Reporting Integration will eventually be an extremely powerful
tool in the hands of developers and radiologist. Developers will be able
to write Machines that output the presence of *Findings* or output quantitative
*Measurements*. EnvoyAI will be able to send the Findings and Measurements
to the radiology reporting system, which will be able to enhance the radiology
workflow in a number of ways:

* Automatically Copying Measurements into a report.
* Automatically checking to make sure a clinical finding was reported,
and warning the radiologist if it is missing.

### How to use the Findings Reporting Interface
The EnvoyAI Findings Reporting Interface is designed to be easy to use.
* Declare a property(s) in your `com.envoyai.schema-out`, depending on the
datatype this can communicate different meanings. In this example we will
just work with `boolean` properties, but for how other datatypes work within
this framework please see [REF.md](../REF.md/#/com.envoyai.report).
* Set a value to the property(s) with the Machine's executable by writing
a string ("true" or "false", if its a boolean field, or a code expression
if its a string field) to file with the properties name in /envoyai/output).
* Create a `com.envoyai.report` LABEL in your dockerfile
* Set the value of the LABEL to a JSON or YAML object with a `findings`
property.
* For each findings property you have declared, add an object that consists
of three parts:
    * A `code` string, representing a code in the referenced coding system
    which represents the finding you wish to communicate.
    * A `code-system` string, representing a coding system (for example snomed-ct)
    * A `value` pointer object, referencing the findings boolean property.
    ```Dockerfile
    LABEL com.envoyai.report="\
    findings:\n\
      - code: '36118008'\n\
        code-system: snomed-ct\n\
        value:\n\
          pointer:\n\
            source: output\n\
            property: pneumothorax\n\
      - code: 'RID5350'\n\
        code-system: radlex\n\
        value:\n\
          pointer:\n\
            source: output\n\
            property: pneumonia-present"
    ```