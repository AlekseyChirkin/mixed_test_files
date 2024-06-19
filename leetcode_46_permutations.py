from itertools import permutations


def permute(nums):
    return permutations(nums)


if __name__ == "__main__":
    for x in permute([1, 2, 3]):
        print(x)
