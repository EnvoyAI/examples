FROM ubuntu:16.04
#LABEL maintainer jaketaylorpro@gmail.com

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

ENTRYPOINT ["./build/examples/cpp_classification/classification.bin","models/bvlc_reference_caffenet/deploy.prototxt","models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel","data/ilsvrc12/imagenet_mean.binaryproto","data/ilsvrc12/synset_words.txt","/mccoy/input/image.jpg"]
CMD []