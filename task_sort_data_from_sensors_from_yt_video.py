import random
import datetime

DATA_COUNT = 3

# prepare data for task
data = [[(str(random.randint(1000000000, 10000000000)) +
        ' neurodivergence.altitude.z0 ' + str(random.randint(1, 1000000))) for x in range(DATA_COUNT)] for i in range(DATA_COUNT)]


def combine_sensors_data(*args: list) -> list:  # Solution #1
    all_lists = []
    for arg in args:
        all_lists.extend(arg)
    return sorted(all_lists, key=lambda x: (int(x.split(' ')[0]), int(x.split(' ')[2])))


def combine_sensors_data2(*args: list) -> list:  # Solution #2
    return args


# Solution #1 time
time1 = datetime.datetime.now()
res1 = combine_sensors_data(*data)
delta_time = datetime.datetime.now() - time1
print(f'Processing time solution #1 is {delta_time} seconds')

# Solution #2 time
time1 = datetime.datetime.now()
res1 = combine_sensors_data2(*data)
delta_time = datetime.datetime.now() - time1
print(f'Processing time solution #2 is {delta_time} seconds')

for x in res1:
    print(x)
