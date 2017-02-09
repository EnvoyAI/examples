import os
import sys
import functools
from dateutil import parser as dateutil_parser
import simplejson as json


def build_path(path):
    if 'MCCOY_DEV' in os.environ and os.environ['MCCOY_DEV'] == 'true':
        return functools.reduce(
            lambda acc, v: acc + '\\' + v,
            filter(lambda o: len(o) > 0, path.split('/')),
            'C:\\Git\mccoy_examples\\test\\test-echo')
    else:
        return path


def open_path(path, mode):
    return open(build_path(path), mode=mode)


def does_path_exist(path):
    return os.path.exists(build_path(path))


schema = {
    "title": "test_echo",
    "type": "object",
    "properties": {
        "test-string": {"type": "string", "title": "test-string"},
        "test-date": {"type": "string", "format": "date-time", "title": "test-date"},
        "test.jpg": {"type": "string", "format": "base64", "title": "test.jpg", "_mime-type": "image/jpg"},
        "test-integer": {"type": "integer", "title": "test-integer"},
        "test-float": {"type": "number", "title": "test-float"},
        "test-percentage": {"type": "number", "title": "test-percentage", "format": "percentage"},
        "test-bool": {"type": "boolean", "title": "test-bool"},
        "test-enum": {"type": "string", "enum": ["A", "B", "C"], "title": "test-enum"},
        # "test-array": {"type": "array", "items": {"type": "string", "format": "uri"}, "title": "test-array"},
        # "test-object": {
        #     "type": "object",
        #     "properties": {
        #         "test-object-string": {"type": "string", "title": "test-object-string"},
        #     },
        #     "title": "test-object"
        # }
    }
}
# respond to the metadata prompt by writing to stdout, with the id, schemas, and info
if len(sys.argv) == 2 and sys.argv[1] == '--metadata':
    sys.stdout.write(json.dumps({
        "model_id": "test/echo",
        "schema_in": schema,
        "schema_out": schema,
        "info": {
            "name": "Test Echo Machine",
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
if does_path_exist('/mccoy/input/test-string'):
    with open_path('/mccoy/input/test-string', 'r') as file_in, \
            open_path('/mccoy/output/test-string', 'w') as file_out:
        test_string = file_in.read()
        file_out.write(test_string)

if does_path_exist('/mccoy/input/test-date'):
    with open_path('/mccoy/input/test-date', 'r') as file_in, \
            open_path('/mccoy/output/test-date', 'w') as file_out:
        test_date_string = file_in.read()
        test_date = dateutil_parser.parse(test_date_string)
        file_out.write(str(test_date))

if does_path_exist('/mccoy/input/test.jpg'):
    with open_path('/mccoy/input/test.jpg', 'rb') as file_in, \
            open_path('/mccoy/output/test.jpg', 'wb') as file_out:
        data = file_in.read()
        file_out.write(data)

if does_path_exist('/mccoy/input/test-integer'):
    with open_path('/mccoy/input/test-integer', 'r') as file_in, \
            open_path('/mccoy/output/test-integer', 'w') as file_out:
        test_integer_string = file_in.read()
        test_integer = int(test_integer_string)
        file_out.write(str(test_integer))

if does_path_exist('/mccoy/input/test-float'):
    with open_path('/mccoy/input/test-float', 'r') as file_in, \
            open_path('/mccoy/output/test-float', 'w') as file_out:
        test_float_string = file_in.read()
        test_float = float(test_float_string)
        file_out.write(str(test_float))

if does_path_exist('/mccoy/input/test-percentage'):
    with open_path('/mccoy/input/test-percentage', 'r') as file_in, \
            open_path('/mccoy/output/test-percentage', 'w') as file_out:
        test_percentage_string = file_in.read()
        test_float = float(test_percentage_string.replace('%', ''))
        file_out.write(str(test_float) + '%')

if does_path_exist('/mccoy/input/test-bool'):
    with open_path('/mccoy/input/test-bool', 'r') as file_in, \
            open_path('/mccoy/output/test-bool', 'w') as file_out:
        test_bool_string = file_in.read()
        test_bool = test_bool_string == 'True'
        file_out.write(str(test_bool))

if does_path_exist('/mccoy/input/test-enum'):
    with open_path('/mccoy/input/test-enum', 'r') as file_in, \
            open_path('/mccoy/output/test-enum', 'w') as file_out:
        test_enum = file_in.read()
        file_out.write(test_enum)

# # make the dir to hold test array
# os.mkdir(build_path('/mccoy/output/test-array'))
#
# with open_path('/mccoy/input/test-array/0', 'r') as file_in_0, \
#         open_path('/mccoy/input/test-array/1', 'r') as file_in_1, \
#         open_path('/mccoy/input/test-array/2', 'r') as file_in_2, \
#         open_path('/mccoy/output/test-array/0', 'w') as file_out_0, \
#         open_path('/mccoy/output/test-array/1', 'w') as file_out_1, \
#         open_path('/mccoy/output/test-array/2', 'w') as file_out_2:
#     test_uri_0 = file_in_0.read()
#     test_uri_1 = file_in_1.read()
#     test_uri_2 = file_in_2.read()
#     file_out_0.write(test_uri_0)
#     file_out_1.write(test_uri_1)
#     file_out_2.write(test_uri_2)
#
# # make the dir to hold test object
# os.mkdir(build_path('/mccoy/output/test-object'))
#
# with open_path('/mccoy/input/test-object/test-string', 'r') as file_in, \
#         open_path('/mccoy/output/test-object/test-string', 'w') as file_out:
#     test_string = file_in.read()
#     file_out.write(test_string)

exit(0)
