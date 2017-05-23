# Echo Example
This example demonstrates each type of input and output parameter and 
how they can be used to gather and display a rich set of data

* [Input Controls](#1-input)
    * [String](#11-simple-inputs)
    * [File](#12-file-inputs)
        * [Image](#121-images)
    * [Nested Object](#13-nested-object-inputs)
    * [Array](#14-array-inputs)
* [Output](#2-output)
    * [String](21-string)
        * [Paragraph](211-paragraph)
    * [DateTime](#22-datetime)
    * [File](#23-file)
        * [Image](#231-image)
        * [Download](#232-download)
    * [Enum](#24-enum)
    * [Integer](#25-integer)
    * [Float](#26-float)
        * [Percentage](#261-percentage)
    * [Boolean](#27-boolean)
    * [Array](#28-array)
    * [Nested Object](#29-nested-object)
###### yaml
First an aside about YAML - Each of the JSON metadata fields (`mccoy.schema_in`,`mccoy.schema_out`,`mccoy.info`)
can be specified with JSON, as they have been in each precceding example, or with YAML (a superset of JSON that 
allows us to drop alot of the cumbersome symbols). This is useful for this example because our schemas become 
quite lengthy, and the additional readability goes a long way. See test/echo's [Dockerfile](Dockerfile) for examples. 



## 1 Input

In practice, all inputs defined by your algorithms `mccoy.schema_in` will be supplied via JSON over WebAPI via the 
'McCoy Integration API', and one should not be too concerned with the exact user interface, as it may need to vary 
system to system, or client to client. However for testing and demonstration purposes, at https://secure.mccoymed.com 
we dynamically render input controls for any input type.

##1.1 Simple Inputs
To gather a typical string input, your schema would have the following property

|           |In Code|JSON Schema Property                                                               |Screenshot                               |
|-----------|---------------|-----------------------------------------------------------------------------------|-----------------------------------------|
|String     |`string`           |`test-string: {type: 'string', title: 'test-string'}`                              |![String](screenshots/string.gif)        |
|Paragraph  |`string`           |`test-paragraph: {type: 'string', title: 'test-paragraph','_control': 'textarea'}` |![Paragraph](screenshots/paragraph.gif)  |
|Enum       |`string`           |`test-enum: {type: 'string', 'enum': ['A', 'B', 'C'], title: 'test-enum'}`         |![Enum](screenshots/enum.gif)            |
|DateTime   |ISO-8601           |`test-date: {type: 'string', format: 'date-time', title: 'test-date'}\n\`          |![DateTime](screenshots/datetime.gif)    |
|Boolean    |`True`&#124;`False`|`test-bool: {type: 'boolean', title: 'test-bool'}`                                 |![Boolean](screenshots/boolean.gif)      |
|Integer    |`string`           |`test-integer: {type: 'integer', title: 'test-integer'}`                           |![Integer](screenshots/integer.gif)      |
|Float      |`string`           |`test-float: {type: 'number', title: 'test-float'}`                                |![Float](screenshots/float.gif)          |
|Percentage |`12%`              |`test-percentage: {type: 'number', format: 'percentage', title: 'test-percentage'}`|![Percentage](screenshots/percentage.gif)|

##1.3 Files

![File](screenshots/file.gif)

###1.3.1 Image

![Image](screenshots/image.gif)


##1.8 Array

![Array](screenshots/array.gif)

##1.9 Nested Object

![Object](screenshots/object.gif)


## 2 Output

##2.1 String

###2.1.1 Paragraph

##2.2 DateTime

##2.3 File

###2.3.1 Image

##2.4 Enum

##2.5 Integer

##2.6 Float

###2.6.1 Percentage

##2.7 Boolean

##2.8 Array

##2.9 Nested Object