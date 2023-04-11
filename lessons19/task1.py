#1) range()
# >>>range(3)
# ...0
# ...1
# ...2
# >>>range(1, 4)
# ...1
# ...2
# ...3
# >>>range(1, 8, 2)
# ...1
# ...3
# ...5
# ...7

#2) enumerate()
lst = ['1', '2', '3'] # tuple
# print(list(enumerate(tlp)))
#todo: Есть список цифр строкового типа. Изменить список так,
# чтобы цифры стали integer.
# for ix, value in enumerate(lst): #[(0, '1'), (1, '2'), (2, '3')]
# 	lst[ix] = int(value)

#3) zip(iterable, iterable)

#todo: Реализовать функцию эквивалентную enumerate()

def zip_enum(lst):
	return zip(range(len(lst)), lst)

# for value in zip_enum(lst):
# 	print(value)

# print(list(zip_enum(lst)))

# for value in enumerate(lst):
# 	print(value)



#todo: Создать словарь из двух списков с помощью zip()
# countries = ['USA', 'Russia', 'Japan']
# capitals = ['Washington', 'Moscow', 'Tokyo']
#
# dct = dict(zip(countries, capitals))
# print(dct)

