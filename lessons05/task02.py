""" Напишите функцию falling_sequens(num), которая выводит сумму чисел от нуля до num.
Например num = 4, тогда функция посчитает 1 + 2 + 3 + 4 и напечатает ответ в консоль.
Используйте while и в первую учередь решите сколько нужно переменных"""

def falling_sequens(n): # объявили функцию
    s = 0

    while n != 0:
        s += n  # cумма = сумма = n
        n -= 1
    print(s)
falling_sequens(int(input())) # вызов функции



# num = int(input())
# summa = 0
# while num != 0:
#     summa += num  # сумма = сумма + num
#     num -= 1      # число = число - 1
# print(summa)

# False
# True
# (как объявить функцию) дз