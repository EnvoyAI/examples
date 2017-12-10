# Getting Started - Learn By Example

Developing for the EnvoyAI Platform requires you to:
* [Build a Docker image containing all runtime dependencies of your algorithm](#1-docker)
* [Provide schemas describing the inputs and outputs of your algorithm](#2-schemas)
* [Write an executable script that will run your algorithm reading and writing files as specified in the schemas](#3-executable)
* [Provide display hints](#4-display)
* [Provide feedback directives](#5-feedback)
* [Provide metadata about your algorithm](#6-metadata)

## Learn By Example

We will use our [helloworld](.) example project to demonstrate the development process.

### 1 Docker
First we will show extracts from the helloworld project's [Dockerfile](./Dockerfile).

Notice the __FROM__, and __RUN__ commands that include all the runtime dependencies.
```Dockerfile
FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
```

The __ADD__ command includes the executable [cmd.py](./cmd.py).
```Dockerfile
ADD . /prog
```
If the executable had any supporting files (more source code or trained networks) those would also be included as well.

The __WORKDIR__, __ENTRYPOINT__ and __CMD__ commands all work together to allow the EnvoyAI Platform to run the executable.
```Dockerfile
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []
```
The EnvoyAI Platform will be able to execute your algorithm as if it were running `$ python cmd.py` from a shell.

### 2 Schemas
The __LABELs__ define the required schemas and metadata with JSON or YAML.

Use the __LABEL__ `com.envoyai.schema-in` to specify the [JSON Schema](http://json-schema.org/) describing 
the inputs to your algorithm.
```Dockerfile
LABEL com.envoyai.schema-in="\
hello:\n\
 type: string\n\
 title: hello"
```
Such an input schema as above declares that there will be exactly one input to the algorithm of the datatype 'string'.
Also, it be titled 'hello' and appear first on the testing website.

Don't forget to escape quotes and newlines with a backslash.

Because this is a simple example, the __LABEL__ `com.envoyai.schema-out` specified an identical schema as `com.envoyai.schema-in`. 
Normally the input and output schemas would differ, for example the input schema might describe a DICOM image input, 
and the output schema might describe a certain diagnosis string with a confidence percentage.

### 3 Executable
Next we will show extracts from helloworld project's [cmd.py](./cmd.py) to demonstrate the interaction 
between the schemas and your algorithm.

The input schema specified a single string input with the key `hello`. The executable must read from the file
`/envoyai/input/hello` and it can expect the format to be a simple string 
(as opposed to, for example, an integer or image file).
```python
with open('/envoyai/input/hello', 'r') as file_in:
    test_string = file_in.read()
```

The output schema also specified a single string output with the key `hello`. Therefore the executable must 
write to the file `/envoyai/output/hello`.
```python
with open('/envoyai/output/hello', 'w') as file_out:
    file_out.write('hello ' + test_string)
```
### 4 Display
To suggest how consumers of your algorithm should display, you use the __LABEL__ `com.envoyai.display`

`com.envoyai.display` must contain two ordered lists of _display-elements_, `source-display-group` generally
representing the inputs, and `result-display-group` generally representing the outputs, as well as a `result-summary`
which provides the consumer with a

Each _display-element_ must have a title, id, and content. Title simply suggests how the viewer should label the value,
the id allows you to reference the display element in feedback, the content tells the viewer what to actually show,
usually with a _pointer_ object. A _pointer_ object contains a single property, `pointer`, which in tern has a `source` prop
describing if the value comes from the input or the output of the algorithm, and a `property` prop which will match the name
of the property from either input or output.

In this case we just have a single input property and single output property to show, and we chose to show the output
property as the summary.
```
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: User Input String\n\
      id: in_str\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: hello\n\
result-display-group:\n\
  display-elements:\n\
    - title: Machine Output String\n\
      id: out_str\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: hello\n\
result-summary:\n\
  content:\n\
    pointer:\n\
      source: output\n\
      property: hello"
```
### 5 Feedback
To optionally describe feedback that an end user should provide, you may use the __LABEL__ `com.envoyai.selector`, currently
only the simplest feedback is supported: `accept-reject` will prompt the user to either agree or disagree with the results.
```
LABEL com.envoyai.selector="\
selector-type: accept-reject"
```

This feedback is used to drive the clinical workflow, and will be configurable by the hospital to react differently to each
Machine's feedback

In the future, you will beable to see the feedback from participating sites to provide you with further labled data.
### 6 Metadata
Use the __LABEL__ `com.envoyai.info` to provide information about your algorithm. 

This is where you name the algorithm and list its author(s). 
```Dockerfile
LABEL com.envoyai.info="\
name: Test Hello World\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: EnvoyAI"
```

In the future this metadata will be searchable if you agree to make the algorithm publicly available.

