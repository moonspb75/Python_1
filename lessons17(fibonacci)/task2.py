"""Домашняя работа"""
"""Напишите функцию geom_fib(first=1, second=2, n), которая печатает в консоль первые n
членов ряда чисел сформированному по следующему принципу
  ""Каждый следующий элемент произведение двух предыдущих"" 
например:

>>>geom_fib(6, 1, 2)
...1 # first
...2 # second
...2 # first * second
...4
...8
...32 
"""

def geom_fib(n, first=1, second=2):
    result = 1
    if n == 1:
        print(first)
    elif n == 2:
        print(second)
        print(first)
    else:
        print(second)
        print(first)
        for num in range(n - 2):
            result = first * second
            first = second
            second = result
            print(result)


geom_fib(5)
# 1 2 2 4 8 32 256