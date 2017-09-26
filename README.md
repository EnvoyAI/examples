# McCoy Medical Technologies Developer API Documentation And Examples Repository
[secure.mccoymed.com](https://secure.mccoymed.com)

You built an algorithm that could save lives. What happens next?

Partner with McCoy to distribute your algorithm.

Read this documentation and explore our examples to learn how to integrate your algorithm into the McCoy Platform.

## Basics and Terminology

### Machine
Yor algorithm can be any combination of trained statistical model, neural net, explicit procedure, decision tree or 
anything else you can imagine.
In order for an algorithm to be used on the McCoy Platform, it must be packaged into a container along with its runtime 
requirements, schema information, and other metadata.
We call this packaged container a _machine_.

### Schema
The data that your algorithm evaluates is called its _inputs_, the data your algorithm produces is called its _outputs_.
Both input and outputs must have well defined data type definitions called a _schema_.
The McCoy Platform uses an Json-Schema and some custom extensions to describe the Machine inputs and outputs as well as 
some display information. 

### Accounts, Organizations and Sharing
If you are the first person from your organization to use the McCoy Platform, you can create an account and organization
and log in using your email address as your username. If your organization already exists, you must be invited to join
by one of your coworkers.
Each new organization will be given access to some example machines, the source code of which can be found in this repository.
If you or someone else in your organization creates a new machine, your organization is now considered the _author_ of that machine.


## Examples and References
The best way to learn about how to create a machine on the McCoy Platform is to read the [helloworld walk-through](./test-helloworld/README.md).

To learn more about advanced input and output types, please see the [test-echo](/test-echo/README.md) example.

To see an example that uses a trained network to do image recognition, see the caffe example we adapated for our platform 
[caffe-cpp_classification](../caffe-cpp_classification/).

To learn more about debugging and error handling on the McCoy platform please see the [test-err](../test-err/) example.

To download and install Docker please visit [www.docker.com](https://www.docker.com/get-docker)

To learn more about Docker we recommend reading the [docs](https://docs.docker.com/) or viewing 
[this great pluralsight video](https://www.pluralsight.com/courses/docker-deep-dive).
