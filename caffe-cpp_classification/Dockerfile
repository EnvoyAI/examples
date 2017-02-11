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

ENTRYPOINT ["./build/examples/cpp_classification/classification.bin","models/bvlc_reference_caffenet/deploy.prototxt","models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel","data/ilsvrc12/imagenet_mean.binaryproto","data/ilsvrc12/synset_words.txt","/mccoy/input/image.jpg"]
CMD []

LABEL mccoy.schema_in "{ \
    \"type\": \"object\", \
    \"properties\": { \
        \"image.jpg\": { \
            \"type\": \"string\", \
            \"format\":\"base64\", \
            \"title\":\"test.jpg\", \
            \"_mime-type\":\"image/jpg\", \
            \"_control\":\"file\" \
        } \
    } \
}"
LABEL mccoy.schema_out "{ \
    \"type\": \"object\", \
    \"properties\": { \
        \"guess0\": { \
            \"type\": \"string\", \
            \"title\": \"First Guess\", \
            \"_order\": 1 \
        }, \
        \"conf0\": { \
            \"type\": \"number\", \
            \"format\": \"percentage\", \
            \"title\": \"First Guess Confidence\", \
            \"_order\": 2 \
        }, \
        \"guess1\": { \
            \"type\": \"string\", \
            \"title\": \"Second Guess\", \
            \"_order\": 3 \
        }, \
        \"conf1\": { \
            \"type\": \"number\", \
            \"format\": \"percentage\", \
            \"title\": \"Second Guess Confidence\", \
            \"_order\": 4 \
        }, \
        \"guess2\": { \
            \"type\": \"string\", \
            \"title\": \"Third Guess\", \
            \"_order\": 5 \
        }, \
        \"conf2\": { \
            \"type\": \"number\", \
            \"format\": \"percentage\", \
            \"title\": \"Third Guess Confidence\", \
            \"_order\": 6 \
        } \
    } \
}"
LABEL mccoy.info "{ \
    \"name\": \"Caffe Example C++ Classification\", \
    \"title\": \"Caffe C++ Classification Example adapted for the mccoy platform.\", \
    \"abstract\": \"N/a\", \
    \"date_trained\": \"N/a\", \
    \"data_source\": \"ilsvrc training set\", \
    \"ground_truth\": \"N/a\", \
    \"algorithm\": \"Neural Net\", \
    \"performance\": \"N/a\", \
    \"fda_status\": \"N/a\" \
}"