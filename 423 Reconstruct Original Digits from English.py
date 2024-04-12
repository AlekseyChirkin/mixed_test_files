# 423. Reconstruct Original Digits from English
from collections import Counter


def originalDigits(s: str) -> str:
    """
        zero: Only digit with z
        two: Only digit with w
        four: Only digit with u
        six: Only digit with x
        eight: Only digit with g
        """

    DIGITS_STR = ("zero", "one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine")
    num = [_ for _ in range(10)]
    cnt = Counter(s)

    num[0] = cnt['z']
    num[2] = cnt['w']
    num[4] = cnt['u']
    num[6] = cnt['x']
    num[8] = cnt['g']
    num[5] = cnt['f'] - num[4]
    num[1] = cnt['o'] - num[2] - num[4] - num[0]
    num[3] = cnt['h'] - num[8]
    num[7] = cnt['v'] - num[5]
    num[9] = cnt['i'] - num[5] - num[6] - num[8]

    return ''.join(sorted([str(i) * freq for i, freq in enumerate(num)]))

    # DIGITS_STR = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

    # def remove_word_from_string(s: str, condition_char: str, num: int, result: str):
    #     while condition_char in s:
    #         for ch in DIGITS_STR[num]:
    #             s = s.replace(ch, '', 1)
    #         result += str(num)
    #     return (s, result)

    # result = ''

    # s, result = remove_word_from_string(s, 'z', 0, result)
    # s, result = remove_word_from_string(s, 'w', 2, result)
    # s, result = remove_word_from_string(s, 'u', 4, result)
    # s, result = remove_word_from_string(s, 'f', 5, result)
    # s, result = remove_word_from_string(s, 'x', 6, result)
    # s, result = remove_word_from_string(s, 'g', 8, result)
    # s, result = remove_word_from_string(s, 'o', 1, result)
    # s, result = remove_word_from_string(s, 'h', 3, result)
    # s, result = remove_word_from_string(s, 'v', 7, result)
    # s, result = remove_word_from_string(s, 'n', 9, result)

    # return ''.join(sorted(result))


if __name__ == "__main__":
    str_for = "owoztneoer"
    res = originalDigits(str_for)
    print(res)
