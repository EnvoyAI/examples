import sys

# read from /input and write to /output

with open('/mccoy/input/hello', 'r') as file_in, \
        open('/mccoy/output/hello', 'w') as file_out:
    test_string = file_in.read()
    file_out.write('hello ' + test_string)

sys.exit(0)
