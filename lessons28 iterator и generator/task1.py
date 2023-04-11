# todo: что такое iterable
# Это перебираемые типы:
string = 'hi'
lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {1: 'word', 2: 'word'}


# todo: определение итератора и генератора

# Итератор – это объект, который поддерживает функцию next()
# для перехода к следующему элементу коллекции.

# Генератор – это итератор, элементы которого
# можно перебирать (итерировать) только один раз

# todo: примеры итераторов
# 1)map
# 2)enumerate
# 3)zip


# todo: получение итераторов явным приведением
# a = iter(string)
# b = iter(lst)
# c = iter(tpl)
# d = iter(dct)

# print(next(d))
# print(next(d))
# print(next(d))


# todo: операции поддерживаемые итераторами
# for it in a:
# 	print(it)

# todo: синтаксис функции-генератора
def get_to_hundred():
    yield list(range(100))


# print(next(get_to_hundred()))
# for item in get_to_hundred():
# 	print(item)
# print(next(d))
# print(next(d))

# print(a, end='\n')
# todo: генератор чисел фибоначчи


def fibonacci(n):
    fib1 = 0
    fib2 = 1
    yield fib1
    yield fib2
    for _ in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2


fib = fibonacci(7)
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

for item in fib:
    print(item)

print(list(fib))
