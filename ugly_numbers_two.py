def nthUglyNumber(n: int) -> int:
    def isUgly(b: int) -> bool:
        if b < 1:
            return False
        if b == 1:
            return True
        good = set([2, 3, 5])

        def ugly(a: int, base: int) -> bool:
            if a in good:
                return True
            if a % base != 0:
                return False
            new_a = a // base
            return ugly(new_a, 2) or ugly(new_a, 3) or ugly(new_a, 5)

        return ugly(b, 2) or ugly(b, 3) or ugly(b, 5)

    u_nums = []
    i = 0
    while len(u_nums) < n:
        if isUgly(i):
            u_nums.append(i)
        i += 1
    return u_nums[-1]


def nthUglyNumber_second(k: int) -> int:
    ugly = [1]
    two = three = five = 0
    while len(ugly) < k:
        while ugly[two]*2 <= ugly[-1]:
            two += 1
        print(ugly)
        while ugly[three]*3 <= ugly[-1]:
            three += 1
        print(ugly)
        while ugly[five]*5 <= ugly[-1]:
            five += 1
        print(ugly)
        ugly.append(min(ugly[two]*2, ugly[three]*3, ugly[five]*5))
    return ugly[-1]


print(nthUglyNumber_second(10))

# print(nthUglyNumber(10))  # 82944
