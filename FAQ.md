# EnvoyAI Frequently Asked Questions

#### How do I log into the developer portal?
[portal.envoyai.com](https://portal.envoyai.com)

#### How do I learn how to create a machine?
The best way to learn about how to create a machine on the EnvoyAI Platform is to read the [helloworld walk-through](./test-hello/README.md).

#### How do I create a machine that take a Dicom file as input?
To learn more about DICOM input and other advanced input and output types, please see [TYPES.md](TYPES.md).
Yes, to see a simple example that takes a dicom study as input and returns a dicom study as output, see the [test/dicom](./test-dicom) example.

#### How do I provide test or sample data for my machine?
We recommend using Google Drive, or Amazon S3 to publicly host sample images and data. You can then publish a link to that data in your Machine description.

#### How do I quickly adapt an already working dockerfile?
To see an example that uses a trained network to do image recognition, see the caffe example we adapted for our platform 
[caffe-cpp_classification](./caffe-cpp_classification/Dockerfile).

For this example we just needed to specify an __ENTRYPOINT__ that would provide the path for the image input, and write the metadata __LABELs__.
The only other required work was to modify the existing project to write the appropriate output files.
See the [Diff](https://github.com/jaketaylorpro/caffe/commit/a90ddca0e384c04d4d0ec0c49e0e7b07c6f0cb07) in our fork of the Caffe repo.

#### How do I view debugging information about my machine when its running on the platform?
To learn more about debugging and error handling on the EnvoyAI platform please see the [test-err](./test-err/) example.

#### How do I get started with Docker?
To download and install Docker please visit [www.docker.com](https://www.docker.com/get-docker)

To learn more about Docker we recommend reading the [docs](https://docs.docker.com/) or viewing 
[this great pluralsight video](https://www.pluralsight.com/courses/docker-deep-dive).

#### Does EnvoyAI Support CUDA?
The EnvoyAI Platform supports nVidia CUDA 8 and CuDNN 5. If your algorithm require a different version, please contact us and we will try to make it available.

Use the __LABEL__ `com.envoyai.nvidia` to enable CUDA support.
```Dockerfile
LABEL com.envoyai.nvidia=true
```

You will likely want to base your Docker image off of an nVidia example.
```Dockerfile
FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu14.04
```

#### YAML or JSON
Each of the metadata fields (`com.envoyai.schema-in`,`com.envoyai.schema-out`,`com.envoyai.display`,`com.envoyai.selector`,`com.envoyai.info`)
can be specified with JSON, or with YAML (a superset of JSON that allows us to drop a lot of the cumbersome symbols).
An important "gotcha" when using YAML in a Dockerfile LABEL is that, because the way Docker caputures strings, each LABEL must have
explicit newline characters using `\n` at the end of each line, and usually a continuation slash so you will see `\n\` at the end of most lines.
See test/echo's [Dockerfile](./test-echo/Dockerfile) for an example that actually mixes yaml and json for brevity and clarity.