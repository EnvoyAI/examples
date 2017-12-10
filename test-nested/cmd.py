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
            '~/dev/envoyai/examples/test/test-nested')
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
if does_dir_exist('/envoyai/input/test-object'):
    mkdir('/envoyai/output/test-object')
    if does_file_exist('/envoyai/input/test-object/test-string'):
        with open_path('/envoyai/input/test-object/test-string', 'r') as file_in, \
                open_path('/envoyai/output/test-object/test-string', 'w') as file_out:
            test_string = file_in.read()
            file_out.write(test_string)

    if does_file_exist('/envoyai/input/test-object/test-percentage'):
        with open_path('/envoyai/input/test-object/test-percentage', 'r') as file_in, \
                open_path('/envoyai/output/test-object/test-percentage', 'w') as file_out:
            test_percentage_string = file_in.read()
            test_float = float(test_percentage_string.replace('%', ''))/100
            file_out.write(str(test_float*100) + '%')

if does_dir_exist('/envoyai/input/test-keywords-array'):
    mkdir('/envoyai/output/test-keywords-array')
    n = 0  # each entry in an array is a file named by it's index
    while does_file_exist('/envoyai/input/test-keywords-array' + '/' + str(n)):
        subpath_in = '/envoyai/input/test-keywords-array' + '/' + str(n)
        subpath_out = '/envoyai/output/test-keywords-array' + '/' + str(n)
        with open_path(subpath_in, 'r') as file_string_in, \
                open_path(subpath_out, 'w') as file_string_out:
            test_string = file_string_in.read()
            file_string_out.write(test_string)
        n = n + 1

if does_dir_exist('/envoyai/input/test-object-array'):
    mkdir('/envoyai/output/test-object-array')
    n = 0  # each entry in an array is a file named by it's index
    inputDirName = '/envoyai/input/test-object-array' + '/' + str(n)
    outputDirName = '/envoyai/output/test-object-array' + '/' + str(n)
    while does_dir_exist(inputDirName):
        mkdir(outputDirName)
        if does_file_exist(inputDirName + '/' + 'test-string'):
            with open_path(inputDirName + '/' + 'test-string', 'r') as file_in, \
                    open_path(outputDirName + '/' + 'test-string', 'w') as file_out:
                test_string = file_in.read()
                file_out.write(test_string)
        if does_file_exist(inputDirName + '/' + 'test-percentage'):
            with open_path(inputDirName + '/' + 'test-percentage', 'r') as file_in, \
                    open_path(outputDirName + '/' + 'test-percentage', 'w') as file_out:
                test_percentage_string = file_in.read()
                test_float = float(test_percentage_string.replace('%', '')) / 100
                file_out.write(str(test_float * 100) + '%')
        n = n + 1
        inputDirName = '/envoyai/input/test-object-array' + '/' + str(n)
        outputDirName = '/envoyai/output/test-object-array' + '/' + str(n)

if does_dir_exist('/envoyai/input/test-file-array'):
    mkdir('/envoyai/output/test-file-array')
    n = 0  # each entry in an array is a file named by it's index
    while does_file_exist('/envoyai/input/test-file-array' + '/' + str(n)):
        subpath_in = '/envoyai/input/test-file-array' + '/' + str(n)
        subpath_out = '/envoyai/output/test-file-array' + '/' + str(n)
        with open_path(subpath_in, 'rb') as file_bytes_in, \
                open_path(subpath_out, 'wb') as file_bytes_out:
            test_bytes = file_bytes_in.read()
            file_bytes_out.write(test_bytes)
        n = n + 1

exit(0)
