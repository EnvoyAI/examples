FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []
LABEL mccoy.schema_in "{ \
    \"title\": \"test_err\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"err\": {\"type\": \"string\", \"enum\": [\"timeout\", \"invalid_output\", \"uncaught_exception\", \"exit_code\"], \"title\": \"err\" \
    } \
}"
LABEL mccoy.schema_out "{ \
    \"title\": \"test_err\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"out\": {\"type\": \"integer\", \"title\": \"out\"} \
    } \
}"
LABEL mccoy.info "{ \
    \"name\": \"Test Err Machine\", \
    \"title\": \"Test machine for demonstration or error handling purposes only\", \
    \"abstract\": \"N/a\", \
    \"date_trained\": \"N/a\", \
    \"data_source\": \"N/a\", \
    \"ground_truth\": \"N/a\", \
    \"algorithm\": \"N/a\", \
    \"performance\": \"N/a\", \
    \"fda_status\": \"N/a\" \
}"
