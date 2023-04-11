def name(arg): # Объявление функции
	print('I am')

# name()

#todo: задача високосный год.
def yearv(num):
	if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
		print('YES')
	else:
		print('No')

# yearv(1600)
#todo: задача snake_case
def snake_case(name):
	name = name.split("_")
	lst = []
	for word in name:
		lst.append(word.capitalize())
	return "".join(lst)

print(snake_case("snake_case"))