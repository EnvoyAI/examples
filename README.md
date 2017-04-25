# McCoy Medical Technologies Developer API Documentation And Examples Repository

You built an algorithm that could save lives. What happens next?

Partner with McCoy to distribute your algorithm.

Read this documentation and explore our examples to learn how to integrate your algorithm into the McCoy Platform.

## 1 Getting Started
Developing for the McCoy Platform requires you to:
* [Build a Docker image containing all runtime dependencies of your algorithm](#21-docker)
* [Provide schemas describing the inputs and outputs of your algorithm](#22-schemas)
* [Write an executable script that will run your algorithm reading and writing files as specified in the schemas](#23-executable)
* [Provide metadata about your algorithm](#24-metadata)
* [(optional) Toggle CUDA support](#25-cuda)

## 2 Learn By Example

We will use our [helloworld](test-helloworld) project as an example to demonstrate.

### 2.1 Docker
First we will show extracts from the helloworld project's [Dockerfile](test-helloworld/Dockerfile).

Notice the __FROM__, and __RUN__ commands that include all the runtime dependencies.
```Dockerfile
FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install simplejson
```

The __ADD__ command includes the executable [cmd.py](test-helloworld/cmd.py).
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

### 2.2 Schemas
The __LABELs__ define the required schemas and the optional metadata.

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

### 2.3 Executable
Next we will show extracts from helloworld project's [cmd.py](test-helloworld/cmd.py) to demonstrate the interaction 
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
### 2.4 Metadata
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

### 2.5 CUDA
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

## 3 More
To learn more about advanced input and output types, please see the [test-echo](test-echo/) example.

To see an example that uses a trained network to do image recognition, see the caffe example we adapated for our platform 
[caffe-cpp_classification](caffe-cpp_classification/).

To learn more about debugging and error handling on the McCoy platform please see the [test-err](test-err/) example.

To download and install Docker please visit [www.docker.com](https://www.docker.com/get-docker)

To learn more about Docker we reccomend reading the [docs](https://docs.docker.com/) or viewing 
[this great pluralsight video](https://www.pluralsight.com/courses/docker-deep-dive).
