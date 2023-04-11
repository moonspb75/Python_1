# """todo: Функции"""
#
# # todo: Как определить функцию?
#
# def print_hello():
#     print('Hello, Python!')
#
# # todo: Как выполнить вызов функции?
#
# print_hello()
# print_hello()
# print_hello()
#
# # todo: Как вернуть значение из функции?
#
# def get_hello():
#     return 'Hello, Python!'
#     print('Никогда не выполнится')
#
# a = get_hello()
# print(a, type(a))
#
#
# # todo: Зачем функции аргументы?
#
# def get_greeting(name):
#     return f'Hello, {name}! {name}'
#
#
# print(get_greeting('Вася'))
# print(get_greeting('Петя'))
# print(get_greeting('Гарри Топор'))
#
#
# def summa(a, b):
#     return a + b
#
# # todo: Как задать значение аргумента по-умолчанию?
#
# # def summa_2(a, b, c=0, d=0):
# #     return a + b + c + d
#
# # print(summa_2(1, 2), summa_2(1, 2, 3))
#
#
# """ todo: Переменное количество аргументов"""

def cool_summa(a, b, *numbers):
    print(type(numbers), numbers)

    result = a + b

    for i in numbers:
        result += i

    return result
