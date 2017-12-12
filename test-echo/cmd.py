import os
import sys
import functools
from dateutil import parser as dateutil_parser


# --------HELPER FUNCTIONS--------
def build_path(path):
    if 'ENVOYAI_DEV' in os.environ and os.environ['ENVOYAI_DEV'] == 'true':
        return functools.reduce(
            lambda acc, v: acc + '\\' + v,
            filter(lambda o: len(o) > 0, path.split('/')),
            'C:\\Git\envoyai_examples\\test\\test-echo')
    else:
        return path


def open_path(path, mode):
    return open(build_path(path), mode=mode)


def does_file_exist(path):
    return os.path.isfile(path)


def does_dir_exist(path):
    return os.path.isdir(build_path(path))


def mkdir(path):
    return os.mkdir(build_path(path))


# --------MAIN--------
# exit, writing error message to stderr and exiting with non-zero error status if any args are passed
if len(sys.argv) > 1:
    sys.stderr.write('bad arguments')
    sys.exit(1)

# if no args were passed we read from /envoyai/input and write to /envoyai/output
if does_file_exist('/envoyai/input/test-string'):
    with open_path('/envoyai/input/test-string', 'r') as file_in, \
            open_path('/envoyai/output/test-string', 'w') as file_out:
        test_string = file_in.read()
        file_out.write(test_string)

if does_file_exist('/envoyai/input/test-enum'):
    with open_path('/envoyai/input/test-enum', 'r') as file_in, \
            open_path('/envoyai/output/test-enum', 'w') as file_out:
        test_enum = file_in.read()
        file_out.write(test_enum)

if does_file_exist('/envoyai/input/test-date'):
    with open_path('/envoyai/input/test-date', 'r') as file_in, \
            open_path('/envoyai/output/test-date', 'w') as file_out:
        test_date_string = file_in.read()
        test_date = dateutil_parser.parse(test_date_string)
        file_out.write(str(test_date))

if does_file_exist('/envoyai/input/test-bool'):
    with open_path('/envoyai/input/test-bool', 'r') as file_in, \
            open_path('/envoyai/output/test-bool', 'w') as file_out:
        test_bool_string = file_in.read()
        test_bool = test_bool_string.lower() == 'true'
        file_out.write(str(test_bool))

if does_file_exist('/envoyai/input/test-int'):
    with open_path('/envoyai/input/test-int', 'r') as file_in, \
            open_path('/envoyai/output/test-int', 'w') as file_out:
        test_int_string = file_in.read()
        test_int = int(test_int_string)
        file_out.write(str(test_int))

if does_file_exist('/envoyai/input/test-float'):
    with open_path('/envoyai/input/test-float', 'r') as file_in, \
            open_path('/envoyai/output/test-float', 'w') as file_out:
        test_float_string = file_in.read()
        test_float = float(test_float_string)
        file_out.write(str(test_float))

if does_file_exist('/envoyai/input/test-percentage'):
    with open_path('/envoyai/input/test-percentage', 'r') as file_in, \
            open_path('/envoyai/output/test-percentage', 'w') as file_out:
        test_percentage_string = file_in.read()
        test_float = float(test_percentage_string.replace('%', '')) / 100
        file_out.write(str(test_float * 100) + "%")

if does_file_exist('/envoyai/input/test.zip'):
    with open_path('/envoyai/input/test.zip', 'rb') as file_in, \
            open_path('/envoyai/output/test.zip', 'wb') as file_out:
        data = file_in.read()
        file_out.write(data)

if does_file_exist('/envoyai/input/test.jpg'):
    with open_path('/envoyai/input/test.jpg', 'rb') as file_in, \
            open_path('/envoyai/output/test.jpg', 'wb') as file_out:
        data = file_in.read()
        file_out.write(data)

if does_file_exist('/envoyai/input/test.pdf'):
    with open_path('/envoyai/input/test.pdf', 'rb') as file_in, \
            open_path('/envoyai/output/test.pdf', 'wb') as file_out:
        data = file_in.read()
        file_out.write(data)

exit(0)
