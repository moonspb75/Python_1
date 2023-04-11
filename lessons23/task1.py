"""Напишите 3 функции:
int_input()
float_input()
list_input() # возвращает список заполняемый user-ом
# >>>a = int_input()
<<<5
# >>> a
...5

# >>>list_input()
<<<1-2-3-4
...['1', '2', '3', '4']"""


def int_input():
    return int(input())


# print(int_input())


def float_input():
    return float(input())


# print(float_input())


def list_input(sep=' '):
    return input().split(sep)


print(list_input())
