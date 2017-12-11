# EnvoyAI Machine API - Data types reference


## Reference Table

|Type        |In Code              |JSON Schema Property                               |Single File|Directory|Notes|
|------------|---------------------|---------------------------------------------------|-----------|---------|-----|
|String      |`string`             |`test-string: {type: 'string'}`                    |✓          |         ||
|Enum        |`string`             |`test-enum: {'enum': ['A', 'B', 'C']}`             |✓          |         ||
|DateTime    |`string` in ISO-8601 |`test-date: {type: 'date-time'}`                   |✓          |         ||
|Boolean     |`True` &#124; `False`|`test-bool: {type: 'boolean'}`                     |✓          |         ||
|Integer     |`string` (must parse)|`test-integer: {type: 'integer'}`                  |✓          |         ||
|Float       |`string` (must parse)|`test-float: {type: 'number'}`                     |✓          |         ||
|Percentage  |`string` ex. `12%`   |`test-percentage: {type: 'percentage'}`            |✓          |         ||
|File        |`byte[]`             |`test.zip: {mime-type: 'application/octet-stream'}`|✓          |         ||
|Image       |`byte[]`             |`test.jpg: {mime-type: 'image/jpeg'}`              |✓          |         ||
|PDF         |`byte[]`             |`test.pdf: {mime-type: 'application/pdf'}`         |✓          |         ||
|DICOM Image |`byte[]`             |`test-dicom-image: {dicom-type: 'dicom-image'}`    |✓          |         ||
|DICOM Series|                     |`test-dicom-series: {dicom-type: 'dicom-series'}`  |           |✓        |Directory name will match property name. Each image in the series will be a separate file named by SOPInstanceId with .dcm file extension|
|DICOM Study |                     |`test-dicom-study: {dicom-type: 'dicom-study'}`    |           |✓        |Directory name will match property name. Each series in the study will be a separate directroy named by SeriesInstanceId. Each image in each series will be a separate file named by SOPInstanceId with .dcm file extension|
|Object      |                     |`test-object: {type: 'object', properties:{...}}`  |           |✓        |Directory name will match property name. Each defined properties will appear as a separate file, named by the property name, in the parent directy. Note the ... can be any number a property definitions including file, object, or array types.|
|Array       |                     |`test-array: {type: 'array', items: ...}`          |           |✓        |Directory name will match property name. Each each element in the array will be named by its 0-based index. Note the ... can be any property definition, including file, object, or array types.|
## Primitive Values
#### Reading primitive values
Reading any of the above primative inputs from the provided files in the `/envoyai/input/` directory is very simple. For example:
```python
with open('/envoyai/input/test-string','r') as file_in:
    test_string = file_in.read()
```
when using DateTime, Boolean, Integer, Float or Percentage the transformation step to convert the string into the
correct data type should be trivial in any programming language. Some example code:
```python
from dateutil import parser as dateutil_parser

# parsing examples
test_date = dateutil_parser.parse('2017-05-27T03:40:40Z') # date-times will be in ISO-8601 format
test_bool = 'False' == 'True' # booleans will either be 'True' or 'False'
test_integer = int('1')
test_float = float('3.1415926')
test_percentage_float = float("85%".replace('%', ''))/100.0 # remember to remove the percent sign
```
#### Writing primitive values
Writing any of the above inputs to the output directory `/envoyai/output/` directory is equally simple. For example:
```python
test_string = "hello world"
with open('/envoyai/output/test-string','w') as file_out:
    file_out.write(test_string)
```
when using DateTime, Boolean, Integer, Float or Percentage the transformation step to convert from your programming language's data type
to the string that should be written to a file follows a similar pattern as the input example above. Some example code:
```python
from datetime import datetime

# example values
date_value = datetime.now()
bool_value = False
int_value = 1
float_value = 3.1415926
percentage_value= 0.85

# example strings
date_string = date_value.isoformat()
bool_string = str(bool_value)
int_string = str(int_value)
float_string = str(float_value)
percentage_string = float(percentage_value*100)+'%'

# writing to files
with open('/envoyai/output/test-date','w') as date_out, \
    open('/envoyai/output/test-bool','w') as bool_out, \
    open('/envoyai/output/int-bool','w') as int_out, \
    open('/envoyai/output/float-bool','w') as float_out, \
    open('/envoyai/output/percentage-bool','w') as percentage_out:
    date_out.write(date_string)
    bool_out.write(bool_string)
    int_out.write(int_string)
    float_out.write(float_string)
    percentage_out.write(percentage_string)
```
## File Values
Working with file inputs and outputs on the EnvoyAI platform is very straightforward by design.
Despite the fact that the 'EnvoyAI Integration API' is capable of communicating over Web API, DICOM, DICOM-WS and
other protocols, the Machine developer needs only to read and write files to successfully integrate and can ignore
all of the complexity related to transcoding and transmission.
As a simple demonstration, the code below reads an image and modifies it by adding text.
The input file `/envoyai/input/image.png` can be read normally, and the `image.png` property of the output will
automatically assume the value of the file written to `/envoyai/input/image.png`.
```python
from PIL import Image, ImageDraw, ImageFont

image = Image.open('/envoyai/input/image.png')
draw  = ImageDraw.Draw(image)
font  = ImageFont.truetype('arial.ttf', 20, encoding='unic')
draw.text( (10,10), 'Your Text', fill='#a00000', font=font)
image.save('/envoyai/output/image.png','PNG')
```
## Nested Objects
Data from a nested object input is available in a sub-directory. For example, if the nested properties specified like so:
```yaml
test-object:
  type: object
  properties:
    test-integer: {type: integer}
    test-string: {type: string}
```
they could be read from these corresponding files:

|Property    |File Path                                |
|------------|-----------------------------------------|
|test-integer|`/envoyai/input/test-object/test-integer`|
|test-string |`/envoyai/input/test-object/test-string` |
## Arrays
#### Basic Usage
An array of strings, or any other type, can be defined in the schema by specifying the
`type` in the `items` sub-property.
```yaml
test-keywords-array:
  title: 'test-keywords-array'
  type: 'array'
  items:
    title: 'keyword'
    type: 'string'
```
#### Array of Nested Object
Using array inputs is especially powerful when used with a defined schema to produce a list of nested objects. This
example uses an image url and associated name.
```yaml
test-keywords-array:
  title: 'test-keywords-array'
  type: 'array'
  items:
    title: 'keyword'
    type: 'object'
      properties:
        url: {type: string, title: Image}
        title: {type: string, title: Title}

```
#### File Directory
Array inputs are also useful to accept a number of files for instance in the case of multiple slices of the same image.
In this case the input control is a directory upload form.
```yaml
test-file-array:
  title: 'test-file-array'
  type: 'array'
  items:
    mime-type: 'application/octet-stream'
```
## Dicom Values
The EnvoyAI Platform has special support for DICOM Studies, Series, and Instances

#### Dicom Study
For input properties with `dicom-type: dicom-study`,
each individual SOPInstance will be in a separate file,
named by SOPInstanceID, and organized into subdirectories named
by SeriesInstanceID. This is intended to make it easier to work with,
but is not required for dicom study output. For output properties
with `dicom-type: dicom-study`, one must simply put each SopInstanceId
in a different file, with any name or subdirectory, into the directory
with the appropriate property name.

#### Dicom Series
For input properties with `dicom-type: dicom-series`,
each individual SOPInstance will be in a separate file, in the directory
named for the property. For output properties with
`dicom-type: dicom-series`, each SOPInstance must be in a separate file,
with any name, so long as it is under the directory with the appropriate
property name.

#### Dicom Image
One can work with Input/Output properties with `dicom-type: dicom-image`
just as they would any other single file type.


#### Constraining Properties
You may choose to constrain your input our output in a few ways,
this may make reading input easier, and may improve performance.

|Property                |Example                      |Study|Series|Image|Description|
|------------------------|-----------------------------|-----|------|-----|-----------|
|transfer-syntax-uid     |['1.2.840.10008.1.2']        |✓    |✓     |✓    |Related to `(0002,0010)`, the EnvoyAI Platform will convert the DICOM Study to the specified transfer syntax before providing it to your Machine, when found in an output property, your Machine will be expected to only output DICOM data with the specified syntax.|
|series-related-instances|1                            |     |✓     |     |Similar to Dicom Query Attribute `(0020,1209)`, the number of instances expected in the series.|
|study-related-series    |[1]                          |✓    |      |     |Inspired by `(0020,1206)` and `(0020,1209)`, this is a list, with one entry per series, containing the number of instances in that series.|
|study-related-instances |1                            |✓    |      |     |Inspired by `(0020,1206)` and `(0020,1209)`, this is a list, with one entry per series, containing the number of instances in that series.|
|sop-classes             |['1.2.840.10008.5.1.4.1.1.1']|✓    |✓     |✓    |Similar to `(0008,0062)`, a list of all SOP Classes contained in the study.|
|modalities              |['CR']                       |✓    |✓     |✓    |Similar to `(0008,0061)`, a list of all Modalities contained in the study.|


#### Descriptive Properties
You may choose to describe the study in various ways to help describe,
but these won't be used in any automated or programmatic way.

|Property                 |Example                      |Study|Series|Image|Description|
|-------------------------|-----------------------------|-----|------|-----|-----------|
|study-description        |upper extremities            |✓    |✓     |✓    |An example value that may appear in `(0008,1030)`|
|series-description       |hand AP                      |     |✓     |✓    |An example value that may appear in `(0008,103e)`|
|series-descriptions-array|['hand AP']                  |✓    |      |     |An example value, per series that may appear in `(0008,103e)`|