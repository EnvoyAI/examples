import sys

# read from /input and write to /output

with open('/envoyai/input/name', 'r') as file_in, \
        open('/envoyai/output/hello', 'w') as file_out:
    test_string = file_in.read()
    file_out.write(test_string + ', come with me if you want to live - modified 2.')

sys.exit(0)
