import time
import sys

# --------MAIN--------
# read in the type of error that we want to test, and do it
print('enter test_err')
with open('/mccoy/input/err', 'r') as file_in, \
        open('/mccoy/output/out', 'w') as file_out:
    err_to_perform = file_in.read()
    if err_to_perform == 'timeout':
        print('about to sleep for 10 minutes')
        time.sleep(600)  # sleep for 10 minutes
        print('done sleeping')
    elif err_to_perform == 'invalid_output':
        file_out.write('non-integer')
        print('wrote a non-integer to an integer field')
    elif err_to_perform == 'uncaught_exception':
        print('about to raise example exception', file=sys.stderr)
        raise Exception('example exception')
    else:
        print('exiting with code 1')
        exit(1)
exit(0)
