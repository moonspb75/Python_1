"""Напишите функцию multiply(a, b) которая будет печатать в
консоль результат умножения "a" на "b"
Например:
multiply(2, 2)
# >>>4
multiply(3, 5)
# >>>15
Ps: пункты 2 и 3 текущей лекции содержат решение д.з."""


def multiply(a, b):
    result = 0
    for i in range(b):
        result = result + a
    print(result)


# multiply(2, 2)

# result = 0
# a = int(input())
# for num in range(a):
#     result = result + int(input())
# print(result)



def degree(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result

assert degree(2, 3) == 2 ** 3


# result = 0
# n = int(input())
#
# for num in range(n + 1):
#     result += num ** 3
# print(result)

result = 1
n = int(input())

for num in range(1,  n):
    result += num * 2
print(result)