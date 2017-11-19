FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install python-dateutil
ADD . /prog
WORKDIR /prog
ENTRYPOINT ["python","cmd.py"]

LABEL com.envoyai.schema-in="\
test-integer:\n\
  type: integer\n\
  title: test-integer" \
    com.envoyai.schema-out="\
test-integer:\n\
  type: integer\n\
  title: test-integer\n\
test-img-bars:\n\
  mime-type: image/png\n\
  title: test-img-bars\n\
test-integer-plus-one:\n\
  type: integer\n\
  title: test-integer" \
    com.envoyai.info="\
name: Test Post-Processing Machine\n\
title: Test machine for demonstration or testing purposes only\n\
author: Staff\n\
organization: McCoy Medical Technologies\n\
abstract: N/a\n\
date_trained: N/a\n\
data_source: N/a\n\
ground_truth: N/a\n\
algorithm: N/a\n\
performance: N/a\n\
fda_status: N/a" \
    com.envoyai.var.url-1="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/SMPTE_Color_Bars.svg/329px-SMPTE_Color_Bars.svg.png" \
    com.envoyai.var.url-2="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/PM5544_with_non-PAL_signals.png/320px-PM5544_with_non-PAL_signals.png" \
    com.envoyai.postprocess.test-img-bars="vars['url-1']" \
    com.envoyai.postprocess.test-integer-plus-one="output['test-integer'] && output['test-integer']+1"