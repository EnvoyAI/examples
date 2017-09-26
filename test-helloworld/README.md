# Getting Started - Learn By Example

Developing for the McCoy Platform requires you to:
* [Build a Docker image containing all runtime dependencies of your algorithm](#1-docker)
* [Provide schemas describing the inputs and outputs of your algorithm](#2-schemas)
* [Write an executable script that will run your algorithm reading and writing files as specified in the schemas](#3-executable)
* [Provide metadata about your algorithm](#4-metadata)
* [(optional) Toggle CUDA support](#5-cuda)

## Learn By Example

We will use our [helloworld](.) example project to demonstrate.

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

The __WORKDIR__, __ENTRYPOINT__ and __CMD__ commands all work together to allow the McCoy Platform to run the executable.
```Dockerfile
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []
```
The McCoy Platform will be able to execute your algorithm as if it were running `$ python cmd.py` from a shell.

### 2 Schemas
The __LABELs__ define the required schemas and metadata with JSON or YAML.

Use the __LABEL__ `mccoy.schema_in` to specify the [JSON Schema](http://json-schema.org/) describing 
the inputs to your algorithm.
```Dockerfile
LABEL mccoy.schema_in "{ \
    \"title\": \"test_hello\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"hello\": {\"type\": \"string\", \"title\": \"hello\", \"_order\": 1} \
    } \
}"
```
Such an input schema as above declares that there will be exactly one input to the algorithm of the datatype 'string'.
Also, it be titled 'hello' and appear first on the testing website.

Don't forget to escape quotes and newlines with a backslash.

Because this is a simple example, the __LABEL__ `mccoy.schema_out` specified an identical schema as `mccoy.schema_in`. 
Normally the input and output schemas would differ, for example the input schema might describe a DICOM image input, 
and the output schema might describe a certain diagnosis string with a confidence percentage.

### 3 Executable
Next we will show extracts from helloworld project's [cmd.py](./cmd.py) to demonstrate the interaction 
between the schemas and your algorithm.

The input schema specified a single string input with the key `hello`. The executable must read from the file
`/mccoy/input/hello` and it can expect the format to be a simple string 
(as opposed to, for example, an integer or image file).
```python
with open('/mccoy/input/hello', 'r') as file_in:
    test_string = file_in.read()
```

The output schema also specified a single string output with the key `hello`. Therefore the executable must 
write to the file `/mccoy/output/hello`.
```python
with open('/mccoy/output/hello', 'w') as file_out:
    file_out.write('hello ' + test_string)
```
### 4 Metadata
Use the __LABEL__ `mccoy.info` to provide information about your algorithm. 

This is where you name the algorithm and list it's author(s). 
```Dockerfile
LABEL mccoy.info "{ \
    \"name\": \"Test Hello World\", \
    \"title\": \"Test machine for demonstration or testing purposes only\", \
    \"author\": \"Staff\", \
    \"organization\": \"McCoy Medical Technologies\", \
    \"abstract\": \"N/a\", \
    \"date_trained\": \"N/a\", \
    \"data_source\": \"N/a\", \
    \"ground_truth\": \"N/a\", \
    \"algorithm\": \"N/a\", \
    \"performance\": \"N/a\", \
    \"fda_status\": \"N/a\" \
}"
```

In the future this metadata will be searchable if you agree to make the algorithm publicly available.

### 5 CUDA
The McCoy Platform supports CUDA 8 and CudNN 5. If you require a different version, please contact us and we will 
find a way to set it up for you.

Use the __LABEL__ `mccoy.nvidia` to toggle on CUDA support.
```Dockerfile
LABEL mccoy.nvidia True
```

You will likely want to base your Docker image off of an nvidia example.
```Dockerfile
FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu14.04
```
