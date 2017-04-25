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
        file_out.write(str(1))
        exit(0)
    elif err_to_perform == 'invalid_output':
        file_out.write('non-integer')
        print('wrote a non-integer to an integer field')
        exit(0)
    elif err_to_perform == 'no_output':
        print('not writing to file')
        exit(0)
    elif err_to_perform == 'large_output':
        for i in range(10000000):
            print('aaaaaaaaaaaaaaaaaaaa' + str(i))
        file_out.write(str(1))
        exit(0)
    else:
        print('received instruction ' + err_to_perform + 'exiting with code 1')
        file_out.write(str(1))
        exit(1)
