# todo: перечислить iterable-типы
tpl = (1, 2, 3)
lst = [1, 2, 3]
dct = {'key': 'value', 'key1': 'value'}
srtring = 'String'


# todo: синтаксис for
# for i in srtring:
# 	print(i, end='')

# todo: синтаксис for range
# range(stop)
# range(start, stop)
# range(start, stop, step)
# for i in range(0, 101, 5):
# print(i, end='-')

# todo: написать функцию выводящую все числа от A до B включительно.
# числа A и B (при этом A ≤ B) получить обоими способами.
def from_a_to_b(a, b):
    for i in range(a, b + 1):
        print(i)


# from_a_to_b(1, 10)

# todo: написать функцию выводящую все числа от A до B включительно.
# числа A и B (при этом B ≤ A) получить как аргументы.
# def from_b_to_a(b, a):
    for i in range(b, a - 1, -1):
        print(i)


# from_b_to_a(10, 0)

# todo: if

# a = 7
# b = 5

# if a < b:
# 	print(a)
# elif a == b:
# 	print(a)
# else:
# 	print(b)

# todo: написать функцию выводящую все числа от A до B включительно.

def from_a_to_b(a, b):
    if a > b:
        step = -1
    else:
        step = 1

    for i in range(a, b + step, step):
        print(i)


# from_a_to_b(1, 10)

# todo: написать  функцию, суммирующую элементы списка.
# список как аргумент
# lst = [5, 7, 8, 10]


# def lst_sum(lst1):
#     result = 0
#     for el in lst1:
#         result += el
#     print(result)
#

# lst_sum(lst)
# todo: написать  функцию, печатающую сумму чисел до n.
# n как аргумент.

