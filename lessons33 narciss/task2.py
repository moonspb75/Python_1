# todo: Напишите функцию принимающую от пользователя 10 int чисел.
# Вычислите их сумму. Напишите программу, использующую наименьшее число
# переменных(1 или 2).


def take_ten_num():
    result = 0
    for i in range(10):
        result += int(input())
    print(result)


take_ten_num()
