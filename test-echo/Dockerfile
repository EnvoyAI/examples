FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install python-dateutil
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]
CMD []
LABEL mccoy.schema_in "{ \
    \"title\": \"test_echo\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"test-string\": {\"type\": \"string\", \"title\": \"test-string\", \"_order\": 1}, \
        \"test-paragraph\": {\"type\": \"string\", \"title\": \"test-paragraph\", \"format\": \"paragraph\", \"_order\": 2, \"_control\": \"textarea\"}, \
        \"test-date\": {\"type\": \"string\", \"format\": \"date-time\", \"title\": \"test-date\", \"_order\": 3}, \
        \"test.jpg\": {\"type\": \"string\", \"format\": \"base64\", \"title\": \"test.jpg\", \"_mime-type\": \"image/jpg\", \"_order\": 4, \"_control\": \"file\"}, \
        \"test.zip\": {\"type\": \"string\", \"format\": \"base64\", \"title\": \"test.zip\", \"_mime-type\": \"application/octet-stream\", \"_order\": 5, \"_control\": \"file\"}, \
        \"test-enum\": {\"type\": \"string\", \"enum\": [\"A\", \"B\", \"C\"], \"title\": \"test-enum\", \"_order\": 6}, \
        \"test-integer\": {\"type\": \"integer\", \"title\": \"test-integer\", \"_order\": 7}, \
        \"test-float\": {\"type\": \"number\", \"title\": \"test-float\", \"_order\": 8}, \
        \"test-percentage\": {\"type\": \"number\", \"title\": \"test-percentage\", \"format\": \"percentage\", \"_order\": 9}, \
        \"test-bool\": {\"type\": \"boolean\", \"title\": \"test-bool\", \"_order\": 10}, \
        \"test-img-url\": {\"type\": \"string\", \"title\": \"test-img-url\", \"_order\": 11} \
    } \
}"
LABEL mccoy.schema_out "{ \
    \"title\": \"test_echo\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"test-string\": {\"type\": \"string\", \"title\": \"test-string\", \"_order\": 1}, \
        \"test-paragraph\": {\"type\": \"string\", \"title\": \"test-paragraph\", \"format\": \"paragraph\", \"_order\": 2, \"_control\": \"textarea\"}, \
        \"test-date\": {\"type\": \"string\", \"format\": \"date-time\", \"title\": \"test-date\", \"_order\": 3}, \
        \"test.jpg\": {\"type\": \"string\", \"format\": \"base64\", \"title\": \"test.jpg\", \"_mime-type\": \"image/jpg\", \"_order\": 4, \"_control\": \"file\"}, \
        \"test.zip\": {\"type\": \"string\", \"format\": \"base64\", \"title\": \"test.zip\", \"_mime-type\": \"application/octet-stream\", \"_order\": 5, \"_control\": \"file\"}, \
        \"test-enum\": {\"type\": \"string\", \"enum\": [\"A\", \"B\", \"C\"], \"title\": \"test-enum\", \"_order\": 6}, \
        \"test-integer\": {\"type\": \"integer\", \"title\": \"test-integer\", \"_order\": 7}, \
        \"test-float\": {\"type\": \"number\", \"title\": \"test-float\", \"_order\": 8}, \
        \"test-percentage\": {\"type\": \"number\", \"title\": \"test-percentage\", \"format\": \"percentage\", \"_order\": 9}, \
        \"test-bool\": {\"type\": \"boolean\", \"title\": \"test-bool\", \"_order\": 10}, \
        \"test-img-url\": {\"type\": \"string\", \"format\": \"imageSrc\", \"title\": \"test-img-url\", \"_mime-type\": \"image/jpg\", \"_order\": 11 } \
    } \
}"
LABEL mccoy.info "{ \
    \"name\": \"Test Echo Machine\", \
    \"title\": \"Test machine for demonstration or testing purposes only\", \
    \"author\": \"Staff\", \
    \"organization\": \"McCoy Medical Technologies\", \
    \"abstract\": \"N/a\", \
    \"date_trained\": \"N/a\", \
    \"data_source\": \"N/a\", \
    \"ground_truth\": \"N/a\", \
    \"algorithm\": \"N/a\", \
    \"performance\": \"N/a\", \
    \"fda_status\": \"N/a\", \
    \"links\": \"N/a\" \
}"