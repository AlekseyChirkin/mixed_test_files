from typing import Counter


def count_frequency(lst: list) -> int:
    return Counter(lst).most_common(1)[0][0]


elements = [2, 3, 2, 4, 5, 6, 4, 5, 2, 4, 4, 4]
frequency = count_frequency(elements)
print(f"Frequency: {frequency}")
