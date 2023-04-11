# todo: напишите lambda-функцию, считающую среднее арифметическое
# от 4-х позиционных аргументов по формуле:
# result = (a1 + a2 + a3 + a4) / 4
avg = lambda a1=1, a2=1, a3=5, a4=5: (a1 + a2 + a3 + a4) / 4
# print(avg(1, 1, 3, 3))

# def avg(a1, a2, a3, a4):
#     print((a1 + a2 + a3 + a4) / 4)
#
#
# avg(1, 1, 3, 3)

# todo: объявленную lambda-функцию, вызовите с распакованным списком
args = [2, 2, 4, 4]
# def args(*lst):
# print(avg(*args))

# todo: напишите lambda-функцию, считающую среднее арифметическое
# от 4-х именованных аргументов по формуле:
# result = (a1 + a2 + a3 + a4) / 4
# print(avg())

# todo: объявленную lambda-функцию , вызовите с распакованным словарём
kwargs = {'a1': 2, 'a2': 2, 'a3': 4, 'a4': 4}
# print(avg(**kwargs))

# todo: Напишите lambda с двумя аргументами a, b считающую
# a + b
s = lambda a, b: a + b
print(s(10, 10))

# # todo: Напишите lambda с двумя аргументами a, b считающую
# # a * b
m = lambda a, b: a * b
print(m(10, 10))
#
# # todo: Напишите lambda с аргументом a считающую
# # a ** 3
p = lambda a: a ** 3
print(p(5))
#
# # todo: Напишите lambda с аргументом string проверяющую
# # является ли переменная строкой
is_str = lambda string: isinstance(string, str)
print(is_str(5))
