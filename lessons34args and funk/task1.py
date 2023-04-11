# todo: написать функцию с четырьмя аргументами и вызвать её
# с аргументом в виде распаковки списка *lst
# def p(a, b, c, d): #args
# 	return a + b + c + d

lines = [4, 3, 7, 6]


# print(p(*lines))


# todo: написать функцию с аргументами по умолчанию
def p(a=0, b=0, c=0, d=0):  # kwargs
    return a + b + c + d


# print(p()) #0
# print(p(1))
# print(p(b=10, d=4, a=1, c=2))
# print(p(1, 3, 7, 9))


# todo: написать функцию с четырьмя именованными аргументами и
# вызвать её с аргументом в виде распаковки словаря **dct
dct = {'a': 10, 'b': 10, 'c': 10, 'd': 10}


# print(p(**dct))

# todo: написать функцию с не фиксированным кол-вом аргументов
# с аргументом в виде распаковки списка *lst

def p(*lst):  # args
    return sum(lst)


print(p(*lines))
print(p(10))
print(p(10, 1, 1, 1, 1))

# на позиционные разбрасываем список *lst
# на именованные разбрасываем словарь **dct

# в функцию с аргументом *args - не фиксированное кол-во аргументов
# или распакованный список.

# todo написать функцию с двумя позиционными аргументами

# todo написать функцию с двумя именованными аргументами

# todo написать функцию с двумя позиционными аргументами
# и вызвать её с распаковкой списка

# todo написать функцию с двумя именованными аргументами
# и вызвать её с распаковкой словаря


# todo: написать функцию с не фиксированным кол-вом аргументов
# с аргументом в виде распаковки списка *lst
