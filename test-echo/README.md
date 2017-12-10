# Echo Example

This example demonstrates each type of input and output parameter and 
how they can be used to gather and display a rich set of data

### 2.2 Nested Object Inputs

#### 2.2.1 Nested Object Input Controls

Nested objects can be used to organize properties - The input controls will be grouped together.

![Object](screenshots/input/object.gif)

#### 2.2.2 Reading Nested Object Input Data

Data from a nested object input is available in a sub-directory. The values of the nested properties of `test-object`: 
* `test-integer`
* `test-float`
* `test-percentage`

can be read from the files: 
* `/envoyai/input/test-object/test-integer`
* `/envoyai/input/test-object/test-float`
* `/envoyai/input/test-object/test-percentage`

### 2.3 Array Inputs

#### 2.3.1 Array of Primitives
`
An array of strings, or any other json-schema primitive, can be defined in the schema by specifying the
`type` in the `items` sub-property.

```yaml
test-keywords-array:
  title: 'test-keywords-array'
  type: 'array'
  items:
    title: 'keyword'
    type: 'string'
```

Arrays will render multiple inputs very similarly to the named inputs in the [Simple Inputs Table](#21-simple-inputs). 
Notice that the array input control requires the user to specify the length of the array first. 

![Array-strings](screenshots/input/array-string.gif)

#### 2.3.2 Array of Nested Objects

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

The input controls follow the same conventions already defined.

![Array-object](screenshots/input/array-object.gif)

Array inputs are also useful to accept a number of files for instance in the case of multiple slices of the same image.
In this case the input control is a directory upload form.
```yaml
test-file-array:
  title: 'test-file-array'
  type: 'array'
  items:
    mime-type: 'application/octet-stream'
```
![Array-dir](screenshots/input/array-dir.gif)

Data from an array input is available in a sub-directory, with each element named by it's index in the array. 
For a string array, a separate string can be read from each individual file which will be named `array-name/0`,
`array-name/1`, `array-name/2`, and so on. Reading data from an array of objects follows all of the above conventions, 
for example `array-name/0/test-int` would contain the value of the `test-int` property of the first element in the 
array named `array-name`.


### 3.2 Nested Object Outputs

Nested object output follows all of the conventions outlined in [Nested Object Input](#22-nested-object-inputs); 
simply create a directory in `/envoyai/output` and put files as property values in the directory.

### 3.3 Array Inputs

Nested object output follows all of the conventions outlined in [Array Input](#23-array-inputs); 
simply create a directory in `/envoyai/output` and put files or directories named by (integer) index with 
files as property values in the directory.
