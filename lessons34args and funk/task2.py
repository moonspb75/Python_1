# todo написать функцию с двумя позиционными аргументами
# def multiply(a, b):
#     return a * b

# print(multiply(5, 5))

# todo написать функцию с двумя именованными аргументами
def multiply(a=5, b=5):
    return a * b


# print(multiply())


# todo написать функцию с двумя позиционными аргументами
# и вызвать её с распаковкой списка
# lst = [2, 2]
# print(multiply(*lst))


# todo написать функцию с двумя именованными аргументами
# и вызвать её с распаковкой словаря

# dct = {'a': 2, 'b': 7}
# print(multiply(**dct))


# todo: написать функцию с не фиксированным кол-вом аргументов
# с аргументом в виде распаковки списка *lst

def multiply(*args):
    result = 1
    for n in args:
        result *= n
    print(result)


multiply(1, 2, 6, 5)
