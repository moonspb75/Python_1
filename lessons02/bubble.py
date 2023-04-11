"""Напишите функцию bubble_sort(lst, desc=False), которая принимает один обязательный аргумент - список из чисел,
выполняет сортировку списка методом пузырька и возвращает получившийся список.
Аргумент desc задает порядок сортировки. Если он равен True, то функция сортирует по убыванию,
если он равен False, то - по возрастанию.
По умолчанию функция сортирует список по возрастанию.
 (!) Запрещено использовать встроенные возможности языка для сортировки."""


def bubble_sort(lst):
    for x in range(len(lst) - 1, 0, - 1):
        for ix in range(x):
            if lst[ix] > lst[ix + 1]:
                lst[ix], lst[ix + 1] = lst[ix + 1], lst[ix]
        print(lst)

lst1 = [9, 4, 8, 2]
bubble_sort(lst1)

# 1) Алгоритм пузырьковой сортировки:

# lst = [9, 7, 5, 4, 1]

# a = 1
# b = 2
# a, b = (b, a)
# a, b = b, a



# for x in range(len(lst) - 1, 0, -1):
# 	# print(x)
# 	for ix in range(x):
# 		if lst[ix] > lst[ix + 1]:
# 			lst[ix], lst[ix + 1] = lst[ix + 1], lst[ix]
# 	print(lst)