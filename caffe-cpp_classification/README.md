# Caffe Classification Example
This example exists to demonstrate how to convert an existing project into one that can be used on the EnvoyAI Platform.

The first step is to build the [Dockerfile](Dockerfile). This project already had a Dockerfile that we could work off of, so getting the runtime dependencies was trivial. 
We just needed to specify an __ENTRYPOINT__ that would provide the path for the image input, and write the metadata __LABELs__.

The next step is to modify the existing project to write the appropriate files. See the [Diff](https://github.com/jaketaylorpro/caffe/commit/a90ddca0e384c04d4d0ec0c49e0e7b07c6f0cb07) in our fork of the Caffe repo.