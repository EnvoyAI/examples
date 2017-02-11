FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install simplejson
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []
LABEL mccoy.schema_in "{ \
    \"title\": \"test_hello\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"hello\": {\"type\": \"string\", \"title\": \"hello\", \"_order\": 1}, \
    } \
}"
LABEL mccoy.schema_out "{ \
    \"title\": \"test_hello\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"hello\": {\"type\": \"string\", \"title\": \"hello\", \"_order\": 1}, \
    } \
}"
LABEL mccoy.info "{ \
    \"name\": \"Test Hello World\", \
    \"title\": \"Test machine for demonstration or testing purposes only\", \
    \"abstract\": \"N/a\", \
    \"date_trained\": \"N/a\", \
    \"data_source\": \"N/a\", \
    \"ground_truth\": \"N/a\", \
    \"algorithm\": \"N/a\", \
    \"performance\": \"N/a\", \
    \"fda_status\": \"N/a\" \
}"