import os
import sys
import simplejson as json

# respond to the metadata prompt by writing to stdout, with the id, schemas, and info
if len(sys.argv) == 2 and sys.argv[1] == '--metadata':
    sys.stdout.write(json.dumps({
        "model_id": "test/helloworld",
        "schema_in": {},
        "schema_out": {},
        "info": {
            "name": "Test Hello World",
            "title": "Test machine for demonstration or testing purposes only",
            "abstract": "N/a",
            "date_trained": "N/a",
            "data_source": "N/a",
            "ground_truth": "N/a",
            "algorithm": "N/a",
            "performance": "N/a",
            "fda_status": "N/a"
        }
    }))
    sys.exit(0)

# exit, writing error message to stderr and exiting with non-zero error status
if len(sys.argv) > 1:
    sys.stderr.write('bad arguments')
    sys.exit(1)

# if no args were passed we read from /input and write to /output

with open('/input/hello', 'r') as file_in, \
        open('/output/hello', 'w') as file_out:
    test_string = file_in.read()
    file_out.write('hello ' + test_string)

sys.exit(0)
