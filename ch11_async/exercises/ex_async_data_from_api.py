import pathlib
import time
import timeit


def get_value_from_api(id):
    lines = pathlib.Path('../data/api_data.txt').read_text().split('\n')
    time.sleep(0.02)
    return int(lines[id])


# TODO: Run the code and write down the output, including the duration from timeit

# TODO: Make get_value_from_api an async coroutine
#   .. and replace time.sleep with the async version

# TODO: Run get_value_from_api 100 times in parallel, once for each id

# TODO: Create the total of the results

# TODO: sum up all the 'value' attributes and print out the total
#   Compare this against the expected value

# TODO: Compare the new time against the old time

def main():
    total = 0
    for i in range(100):
        value = get_value_from_api(i)
        total += value
    print(total)


print(timeit.timeit('main()', number=1, globals=locals()))

# Expected output:
# 53098958
# (plus the time from timeit, e.g. 2.0495059989989386)
