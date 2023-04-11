# var = {}
#
#
# def funktion(variable):
#     return variable
#
#
# print(funktion(var))


# range(start, stop, step)- диапазоны
def sum(stop):
	result = 0
	for num in range(stop + 1):
		result = result + num
	print(result)
sum(3)
# list(range(1,5))
# [1, 2, 3, 4]
# >>> list(range(3, 5))
# [3, 4]
# >>> list(range(3, 8))
# [3, 4, 5, 6, 7]
# >>> list(range(3, 8, 2))
# [3, 5, 7]
# >>> list(range(0, 8, 2))
# [0, 2, 4, 6]
# >>> list(range(1, 8, 2))
# [1, 3, 5, 7]
# >>> list(range(8, 1, -2))
# [8, 6, 4, 2]