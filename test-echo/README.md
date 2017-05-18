# Echo Example
This example demonstrates each type of input and output parameter and 
how they can be used to gather and display a rich set of data

* [Input Controls](#1-input)
    * [String](#11-string)
        * [Paragraph](#111-paragraph)
    * [DateTime](#12-datetime)
    * [File](#13-file)
        * [Image](#131-image)
    * [Enum](#14-enum)
    * [Integer](#15-integer)
    * [Float](#16-float)
        * [Percentage](#161-percentage)
    * [Boolean](#17-boolean)
    * [Array](#18-array)
    * [Nested Object](#19-nested-object)
###### yaml
First an aside about YAML - Each of the JSON metadata fields (`mccoy.schema_in`,`mccoy.schema_out`,`mccoy.info`)
can be specified with JSON, as they have been in each precceding example, or with YAML (a superset of JSON that 
allows us to drop alot of the cumbersome symbols). This is useful for this example because our schemas become 
quite lengthy, and the additional readability goes a long way. See test/echo's [Dockerfile](Dockerfile) for examples. 

## 1 Input

##1.1 String

###1.1.1 Paragraph

##1.2 DateTime

##1.3 File

###1.3.1 Image

##1.4 Enum

##1.5 Integer

##1.6 Float

###1.6.1 Percentage

##1.7 Boolean

##1.8 Array

##1.9 Nested Object