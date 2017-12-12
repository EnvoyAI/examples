FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        python-setuptools \
        python-scipy && \
    rm -rf /var/lib/apt/lists/*

ENV CAFFE_ROOT=/opt/caffe
WORKDIR $CAFFE_ROOT

# FIXME: use ARG instead of ENV once DockerHub supports this
ENV CLONE_TAG=master

RUN git clone -b ${CLONE_TAG} --depth 1 https://github.com/jaketaylorpro/caffe.git . && \
    pip install --upgrade pip && \
    cd python && for req in $(cat requirements.txt) pydot; do pip install $req; done && cd .. && \
    mkdir build && cd build && \
    cmake -DCPU_ONLY=1 .. && \
    make -j"$(nproc)"

RUN /opt/caffe/scripts/download_model_binary.py models/bvlc_reference_caffenet
RUN /opt/caffe/data/ilsvrc12/get_ilsvrc_aux.sh

ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

ENTRYPOINT ["./build/examples/cpp_classification/classification.bin","models/bvlc_reference_caffenet/deploy.prototxt","models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel","data/ilsvrc12/imagenet_mean.binaryproto","data/ilsvrc12/synset_words.txt","/envoyai/input/image.jpg"]

LABEL com.envoyai.metadata-version=2
LABEL com.envoyai.nvidia=false
LABEL com.envoyai.info="\
name: Caffe Example C++ Classification\n\
title: Caffe C++ Classification Example adapted for the EnvoyAI platform.\n\
author: Caffe adapted by EnvoyAI Staff\n\
organization: Caffe and EnvoyAI\n\
data-source: ilsvrc training set\n\
algorithm: Neural Net\n\
links: you can download a frog picture <a href='http://zso3597.cias.rit.edu/256/week4/project1/images/frog.jpg'>here</a>"
LABEL com.envoyai.schema-in="\
image.jpg:\n\
  title: Input Image\n\
  mime-type: image/jpeg"
LABEL com.envoyai.schema-out="\
guess0:\n\
  title: First Guess\n\
  type: string \n\
conf0:\n\
  title: First Guess Confidence\n\
  type: percentage\n\
guess1:\n\
  title: Second Guess\n\
  type: string \n\
conf1:\n\
  title: Second Guess Confidence\n\
  type: percentage\n\
guess3:\n\
  title: Third Guess\n\
  type: string \n\
conf3:\n\
  title: Third Guess Confidence\n\
  type: percentage"
LABEL com.envoyai.display="\
source-display-group:\n\
  display-elements:\n\
    - title: Input Image\n\
      id: input-image\n\
      content:\n\
        pointer:\n\
          source: input\n\
          property: image.jpg\n\
results-display-group:\n\
  presentation: tile\n\
  display-elements:\n\
    - title: First Guess\n\
      id: guess-0\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: guess0\n\
      associated-values:\n\
        - value:\n\
            pointer:\n\
              source: output\n\
              property: conf0\n\
          unit: percentage\n\
          label: Confidence\n\
    - title: Second Guess\n\
      id: guess-1\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: guess1\n\
      associated-values:\n\
        - value:\n\
            pointer:\n\
              source: output\n\
              property: conf1\n\
          unit: percentage\n\
          label: Confidence\n\
    - title: Third Guess\n\
      id: guess-2\n\
      content:\n\
        pointer:\n\
          source: output\n\
          property: guess2\n\
      associated-values:\n\
        - value:\n\
            pointer:\n\
              source: output\n\
              property: conf2\n\
          unit: percentage\n\
          label: Confidence"
LABEL com.envoyai.selector="\
selector-type: choose-one-display-element\n\
selector-config:\n\
  choose-options:\n\
    - guess-0\n\
    - guess-1\n\
    - guess-2\n\
  default-option: guess-0"