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
    \"title\": \"test_post\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"test-integer\": {\"type\": \"integer\", \"title\": \"test-integer\", \"_order\": 1} \
    } \
}"
LABEL mccoy.schema_out "{ \
    \"title\": \"test_post\", \
    \"type\": \"object\", \
    \"properties\": { \
        \"test-integer\": {\"type\": \"integer\", \"title\": \"test-integer\", \"_order\": 1}, \
        \"test-img-bars\": {\"type\": \"string\", \"format\": \"imageSrc\", \"title\": \"test-img-bars\", \"_mime-type\": \"image/jpg\", \"_order\": 2 }, \
        \"test-integer-plus-one\": {\"type\": \"integer\", \"title\": \"test-integer\", \"_order\": 3} \
    } \
}"
LABEL mccoy.info "{ \
    \"name\": \"Test Post-Processing Machine\", \
    \"title\": \"Test machine for demonstration or testing purposes only\", \
    \"author\": \"Staff\", \
    \"organization\": \"McCoy Medical Technologies\", \
    \"abstract\": \"N/a\", \
    \"date_trained\": \"N/a\", \
    \"data_source\": \"N/a\", \
    \"ground_truth\": \"N/a\", \
    \"algorithm\": \"N/a\", \
    \"performance\": \"N/a\", \
    \"fda_status\": \"N/a\" \
}"
LABEL mccoy.var.url-1 "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/SMPTE_Color_Bars.svg/329px-SMPTE_Color_Bars.svg.png"
LABEL mccoy.var.url-2 "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/PM5544_with_non-PAL_signals.png/320px-PM5544_with_non-PAL_signals.png"

LABEL mccoy.postprocess.test-img-bars "vars['url-1']"
LABEL mccoy.postprocess.test-integer-plus-one "output['test-integer'] && output['test-integer']+1"