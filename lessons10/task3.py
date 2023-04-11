"""Напишите функцию sum(start, stop) которая выводит в консоль сумму чисел от start до stop.
Например sum(3, 6) = 3 + 4 + 5 + 6 = 18"""


def sum(start, stop):
    result = 0
    for num in range(start, stop + 1):
        result = result + num
    print(result)



sum(3, 6)






# sum(range(3, 6))

# iterable- объект, поддерживающий итерацию