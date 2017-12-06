import os
import sys
import functools


# --------HELPER FUNCTIONS--------
def build_path(path):
    if 'ENVOYAI_DEV' in os.environ and os.environ['ENVOYAI_DEV'] == 'true':
        return functools.reduce(
            lambda acc, v: acc + '\\' + v,
            filter(lambda o: len(o) > 0, path.split('/')),
            'C:\\Git\envoyai_examples\\test\\test-dicom-echo')
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

# if no args were passed we read from /envoyai/input and write to /envoyai/output
if does_dir_exist('/envoyai/input/test-dicom'):
    mkdir('/envoyai/output/test-dicom')
    n = 0  # each entry in an array is a file named by it's index
    while does_file_exist('/envoyai/input/test-dicom' + '/' + str(n)):
        subpath_in = '/envoyai/input/test-dicom' + '/' + str(n)
        subpath_out = '/envoyai/output/test-dicom' + '/' + str(n)
        with open_path(subpath_in, 'rb') as file_bytes_in, \
                open_path(subpath_out, 'wb') as file_bytes_out:
            test_bytes = file_bytes_in.read()
            file_bytes_out.write(test_bytes)
        n = n + 1
exit(0)
