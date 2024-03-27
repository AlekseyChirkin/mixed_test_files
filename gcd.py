def gcdiv(a: int, b: int) -> int:
    print(f"{a=}, {b=}")
    while b:
        a, b = b, a % b
        print(f"{a=}, {b=}")
    return a


print(gcdiv(4, 10))
