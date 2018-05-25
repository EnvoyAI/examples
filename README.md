# EnvoyAI Developer API Documentation And Examples Repository

You built an algorithm that could save lives. What happens next?

Partner with EnvoyAI to distribute your algorithm!

Read this documentation and explore our examples to learn how to integrate your algorithm into the EnvoyAI Platform.

## EnvoyAI Machine API Version 2

We are now using a new version of the EnvoyAI Machine API. Version 2 has been designed for use with the EnvoyAI Liaison,
our integration appliance, which will enable algorithms to be used in a clinical workflow. Version 1 Machines will continue to work
on the dev portal. Upgrading existing version 1 machines to version 2, is as simple as modifying a few Docker LABELs.
All examples and documentation will now refer to version 2.
Version 1 documentation will remain available in the v2 branch of this repository.

## Basics and Terminology

### Machine
Your algorithm can be any combination of trained statistical model, neural net, explicit procedure, decision tree or
anything else you can imagine.
In order for an algorithm to be used on the EnvoyAI Platform, it must be packaged into a Docker container along with its runtime 
requirements, schema information, and other metadata.
We call this packaged container a _machine_.

### Schema
The data that your algorithm evaluates is called its _inputs_, the data your algorithm produces is called its _outputs_.
Both input and outputs must have well defined data type definitions called a _schema_.
The EnvoyAI Platform uses a system based on JSON-Schema but uses different defaults, and has additional
features to describe files and DICOM studies. Additionally the platform uses a similar schema to define how the inputs 
and outputs are to be displayed. Either JSON or YAML formatted schemas are accepted.

### Accounts, Organizations, and Sharing
If you are the first person from your organization to sign up with the EnvoyAI Platform, you can create an account and organization.
Your email address will be your username. If, however, your organization is already signed up, you must be invited to join
by one of your coworkers to gain access.
Each new organization will be given access to some example machines, the source code of which can be found in this repository.
If you or others in your organization creates a new machine, your organization is now considered the _author_ of that machine.


## Examples and References
The best way to learn about how to create a machine on the EnvoyAI Platform is to read the [helloworld walk-through](./test-hello/README.md).

To learn more about input and output types, please see the [types reference](TYPES.md).

To see a reference for all supported Docker LABELs, please see [REF.md](REF.md).

It is also helpful to read through the [FAQ](FAQ.md)

To see an example that uses a trained network to do image recognition, see the caffe example we adapted for our platform 
[caffe-cpp_classification](./caffe-cpp_classification/).

To see an example that takes a single dicom image as input and uses pydicom and numpy to manipulate dicom image data, look at: [dicom-image](./test-dicom-image)

To see an example that uses a Windows executable, check out: [test-wine](./test-wine)

To see an example that takes 
## Get Started

To log into our site and try it out, visit [portal.envoyai.com](https://portal.envoyai.com).
