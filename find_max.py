import random


def find_maximum(nums: list) -> int:
    max = 0
    i = 0
    for x in nums:
        if x > max:
            max = x
    return max


numbers = [random.randint(1, 99) for x in range(10)]
print(f"Maximum from list {numbers} is {find_maximum(numbers)}.")
