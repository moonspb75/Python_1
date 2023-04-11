""" Напишите функцию sumlist(lst, x), принимающую число "x" и
список цифр, увеличивающую каждый элемент на "x" и печатающую
результат в консоль.
Пример:
nlst = [1, 2, 3, 4]
sumlist(nlst, 2)
<<<[3, 4, 5, 6] #т.е. каждый элемент увеличен на 2"""

nlst = [1, 2, 3, 4]
# nlst = [(0, 1), (1, 2), 3, 4]

def sumlist(lst, x):
	for ix, value in enumerate(lst):
		lst[ix] = value + x
	print(lst)


sumlist(nlst, 2)