import os
import sys
import functools
from dateutil import parser as dateutil_parser


# --------HELPER FUNCTIONS--------
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


# --------MAIN--------
# exit, writing error message to stderr and exiting with non-zero error status if any args are passed
if len(sys.argv) > 1:
    sys.stderr.write('bad arguments')
    sys.exit(1)

# if no args were passed we read from /mccoy/input and write to /mccoy/output
if does_path_exist('/mccoy/input/test-string'):
    with open_path('/mccoy/input/test-string', 'r') as file_in, \
            open_path('/mccoy/output/test-string', 'w') as file_out:
        test_string = file_in.read()
        file_out.write(test_string)

if does_path_exist('/mccoy/input/test-paragraph'):
    with open_path('/mccoy/input/test-paragraph', 'r') as file_in, \
            open_path('/mccoy/output/test-paragraph', 'w') as file_out:
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

if does_path_exist('/mccoy/input/test-img-url'):
    with open_path('/mccoy/input/test-img-url', 'r') as file_in, \
            open_path('/mccoy/output/test-img-url', 'w') as file_out:
        test_img_url = file_in.read()
        file_out.write(test_img_url)

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
