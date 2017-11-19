import sys

# --------MAIN--------
# exit, writing error message to stderr and exiting with non-zero error status if any args are passed
if len(sys.argv) > 1:
    sys.stderr.write('bad arguments')
    sys.exit(1)
# if no args were passed we read from /input and write to /output

with open('/envoyai/input/test-integer', 'r') as file_in, \
        open('/envoyai/output/test-integer', 'w') as file_out:
    test_string = file_in.read()
    file_out.write(test_string)

sys.exit(0)
