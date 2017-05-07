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

# if no args were passed we read from /mccoy/input and write to /mccoy/output
if does_file_exist('/mccoy/input/test-string'):
    with open_path('/mccoy/input/test-string', 'r') as file_in, \
            open_path('/mccoy/output/test-string', 'w') as file_out:
        test_string = file_in.read()
        file_out.write(test_string)

if does_file_exist('/mccoy/input/test-paragraph'):
    with open_path('/mccoy/input/test-paragraph', 'r') as file_in, \
            open_path('/mccoy/output/test-paragraph', 'w') as file_out:
        test_string = file_in.read()
        file_out.write(test_string)

if does_file_exist('/mccoy/input/test-date'):
    with open_path('/mccoy/input/test-date', 'r') as file_in, \
            open_path('/mccoy/output/test-date', 'w') as file_out:
        test_date_string = file_in.read()
        test_date = dateutil_parser.parse(test_date_string)
        file_out.write(str(test_date))

if does_file_exist('/mccoy/input/test.jpg'):
    with open_path('/mccoy/input/test.jpg', 'rb') as file_in, \
            open_path('/mccoy/output/test.jpg', 'wb') as file_out:
        data = file_in.read()
        file_out.write(data)

if does_file_exist('/mccoy/input/test.zip'):
    with open_path('/mccoy/input/test.zip', 'rb') as file_in, \
            open_path('/mccoy/output/test.zip', 'wb') as file_out:
        data = file_in.read()
        file_out.write(data)

if does_file_exist('/mccoy/input/test-integer'):
    with open_path('/mccoy/input/test-integer', 'r') as file_in, \
            open_path('/mccoy/output/test-integer', 'w') as file_out:
        test_integer_string = file_in.read()
        test_integer = int(test_integer_string)
        file_out.write(str(test_integer))

if does_file_exist('/mccoy/input/test-float'):
    with open_path('/mccoy/input/test-float', 'r') as file_in, \
            open_path('/mccoy/output/test-float', 'w') as file_out:
        test_float_string = file_in.read()
        test_float = float(test_float_string)
        file_out.write(str(test_float))

if does_file_exist('/mccoy/input/test-percentage'):
    with open_path('/mccoy/input/test-percentage', 'r') as file_in, \
            open_path('/mccoy/output/test-percentage', 'w') as file_out:
        test_percentage_string = file_in.read()
        test_float = float(test_percentage_string.replace('%', ''))
        file_out.write(str(test_float) + '%')

if does_file_exist('/mccoy/input/test-bool'):
    with open_path('/mccoy/input/test-bool', 'r') as file_in, \
            open_path('/mccoy/output/test-bool', 'w') as file_out:
        test_bool_string = file_in.read()
        test_bool = test_bool_string == 'True'
        file_out.write(str(test_bool))

if does_file_exist('/mccoy/input/test-enum'):
    with open_path('/mccoy/input/test-enum', 'r') as file_in, \
            open_path('/mccoy/output/test-enum', 'w') as file_out:
        test_enum = file_in.read()
        file_out.write(test_enum)

if does_file_exist('/mccoy/input/test-img-url'):
    with open_path('/mccoy/input/test-img-url', 'r') as file_in, \
            open_path('/mccoy/output/test-img-url', 'w') as file_out:
        test_img_url = file_in.read()
        file_out.write(test_img_url)

if does_dir_exist('/mccoy/input/test-img-url-array'):
    mkdir('/mccoy/output/test-img-url-array')
    n = 0  # each entry in an array is a file named by it's index
    while does_dir_exist('/mccoy/input/test-img-url-array' + '/' + str(n)):
        subpath_in = '/mccoy/input/test-img-url-array' + '/' + str(n)
        subpath_out = '/mccoy/output/test-img-url-array' + '/' + str(n)
        mkdir(subpath_out)
        with open_path(subpath_in + '/title', 'r') as file_title_in, \
                open_path(subpath_in + '/image', 'r') as file_image_in, \
                open_path(subpath_out + '/title', 'w') as file_title_out, \
                open_path(subpath_out + '/' + str(n) + '/image', 'w') as file_image_out:
            test_title = file_title_in.read()
            test_img_url = file_image_in.read()
            file_title_out.write(test_title)
            file_image_out.write(test_img_url)
        n = n + 1

exit(0)
