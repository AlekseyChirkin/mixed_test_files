from collections import Counter
import random


def count_frequency(lst: list):
    return sorted(dict(Counter(lst)).items(), key=lambda item: item[1])


elements = [random.randint(1, 100) for x in range(100)]
freq = count_frequency(elements)
most_freq = freq[-1][0]

print(f"{elements=}\n{freq=}\nMost frequent element is {most_freq}")
