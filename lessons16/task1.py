"""
todo: Функции
"""

# todo: Как определить функцию?

def print_hello():
    print('Hello, Python!')

# todo: Как выполнить вызов функции?

# print_hello()
# print_hello()
# print_hello()

# todo: Как вернуть значение из функции?

def get_hello():
    return 'Hello, Python!'
    print('Никогда не выполнится')

a = get_hello()

# print(a, type(a))


# todo: Зачем функции аргументы?

def get_greeting(name):
    return f'Hello, {name}! {name}'


# print(get_greeting('Вася'))
# print(get_greeting('Петя'))
# print(get_greeting('Гарри Топор'))


def summa(a, b):
    return a + b

# a = summa(1, 2) # Эквивалентно print(summa(1, 2))
# print(a)

# todo: Как задать значение аргумента по-умолчанию?

# def summa_2(a, b, c=0, d=0):
#     return a + b + c + d

# print(summa_2(1, 2))
# >>>3
# print(summa_2(1, 3, 5))
# >>>9
# print(summa_2(1, 3, 5, 7))
# >>>16
# print(summa_2(1, 3, d=5))
# >>>9

# print(summa_2(1, 2), summa_2(1, 2, 3))


# todo: Переменное количество аргументов

def cool_summa(a, b, *numbers):

    result = a + b

    for i in numbers:
        result += i

    return result



def get_person(name, age, skills):
    print(f'Имя: {name}, Возраст: {age}, Навыки: {skills}')

me = {'name': 'Sergey',
      'age': 24,
      'skills': ['Coder', 'Teacher']
}

get_person(**me) #me - keyword arguments



# >>>list(range(3)) #start
# ...0
# ...1
# ...2

# >>>list(range(1, 3)) #start, stop
# ...1
# ...2

# >>>list(range(2, 10, 3)) #start, stop, step
# ...2
# ...5
# ...8

# >>>list(range(2, 12, 4)) #start, stop, step
# ...2
# ...6
# ...10

# name = 'Sergey'
# print(f'Hello {name}. How are you?')

