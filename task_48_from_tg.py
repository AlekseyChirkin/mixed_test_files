"""
Создайте функцию infinite(lst, tries), которая будет проходиться по элементам списка lst (целые числа)
заданное количество раз (tries) циклически.  
Один раз - один элемент списка.  
После вывода последнего значения последовательности процедура начнется с самого начала. 
 
Пример:

Если в списке 2 элемента, а функция получила значение 3, то сначала выведется первый объект,
потом последний, а потом опять первый.  
Результат работы функции представьте в виде строки, состоящей из tries количества символов.

Для решения задачи нужно использовать функцию cycle() из модуля itertools. Она перебирает последовательность циклически,
а по мере достижения последнего элемента начинает заново.
"""


from itertools import cycle


def infinite(lst: list, tries: int) -> str:
    result = []
    i = j = 0
    while i < tries:
        result.append(lst[j])
        i += 1
        j += 1
        if j == len(lst):
            j = 0
    return "".join([str(x) for x in result])


def infinite2(lst: list, tries: int) -> str:
    result = []
    i = 0
    while True:
        for n in lst:
            i += 1
            if i > tries:
                return "".join([str(x) for x in result])
            result.append(n)


def infinite3(lst: list, tries: int) -> str:
    result = ""
    cycle_lst = cycle(lst)
    for _ in range(tries):
        result += str(next(cycle_lst))
    return result


if __name__ == "__main__":
    print(infinite3([1, 2, 3, 4, 5, 6, 7, 8, 9], 20))
