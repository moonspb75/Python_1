"""Напишите функцию less(a, b, c) возвращающую наименьшее из трёх чисел"""


def less(a, b, c):

    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
# print(less(4, 1, 3))


def equale(a, b, c):
    if a != b and b != c and a != c:
        return 0
    elif a == b and b == c and a == c:
        return 3
    else:
        return 2
print(equale(1, 2, 2))