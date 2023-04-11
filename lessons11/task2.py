""" Напишите функцию multyple_list(lst, x), принимающую число "x" и
lst - список цифр, увеличевающую каждый элемент в "x" раз и печатающую
результат в консоль.
Пример:
nlst = [1, 2, 3, 4]
multyple_list(nlst, 2)
# >>>[2, 4, 6, 8] #т.е. каждый элемент увеличен в 2 раза"""



nlst = [1, 2, 3, 4]


def multyple_list(lst, x):
    for ix, value in enumerate(lst):
        lst[ix] = value * x
    print(lst)


multyple_list(nlst, 2)