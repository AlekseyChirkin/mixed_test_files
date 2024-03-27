from collections import Counter
import random


def count_frequency(lst: list):
    return sorted(dict(Counter(lst)).items(), key=lambda item: item[1])


def count_frequency2(lst: list):
    return Counter(lst).most_common(1)


elements = [random.randint(1, 100) for x in range(100)]
freq = count_frequency(elements)
most_freq = freq[-1]
print(f"""
      {elements=}\n
      {freq=}\n
      Most frequent element by "sorted and lambda function" is {most_freq}
      """)

freq = count_frequency2(elements)
print(f'Most frequent element by "most_common" function is {freq}')
