# numbers = [x for x in range(10)]
# even_odd_numbers = ['even' if x % 2 == 0 else 'odd' for x in numbers]
# print(numbers)
# print(even_odd_numbers)


# squares = {x: x**2 for x in range(10)}
# print(squares)

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 5],
    [7, 8, 9, 0],
    [57, 78, 95, 100],
]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]


def print_matrix(mat: list):
    for i in mat:
        print(i)
    print("====================")
    pass


print_matrix(matrix)
print_matrix(transposed_matrix)
