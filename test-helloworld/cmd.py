import sys

# --------MAIN--------
# exit, writing error message to stderr and exiting with non-zero error status if any args are passed
if len(sys.argv) > 1:
    sys.stderr.write('bad arguments')
    sys.exit(1)
# if no args were passed we read from /input and write to /output

with open('/mccoy/input/hello', 'r') as file_in, \
        open('/mccoy/output/hello', 'w') as file_out:
    test_string = file_in.read()
    file_out.write('hello ' + test_string)

sys.exit(0)
