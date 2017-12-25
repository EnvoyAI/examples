import os
import sys
import functools


# --------HELPER FUNCTIONS--------
import shutil


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
if does_dir_exist('/envoyai/input/dicom-series-in'):
    # mkdir('/envoyai/output/dicom-study-out')
    # TODO iterate through series and instances
    print("copying whole dicom series to output")
    shutil.copytree('/envoyai/input/dicom-series-in','/envoyai/output/dicom-series-out')
exit(0)
