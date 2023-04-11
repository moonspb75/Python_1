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


def list_sum(lst):
	result = 0
	for num in lst:
		result = result + num
	print(result)

# 3) Выполнить действие n - раз.

for i in range(3):
	print('Ура!')
# >>>Ура!
# >>>Ура!
# >>>Ура!


# while True: - цикл while