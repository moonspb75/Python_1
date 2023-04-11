"""Напишите функцию генератор step_gen(step), где step шаг. Генератор
должен работать от нуля до бесконечности. Для реализации используйте
цикл While.
Пример использования:
>>>a = step_gen(5)
>>>next(a)
...0
>>>next(a)
...5
>>>next(a)
...10
>>>next(a)
...15"""


def step_gen(step):
    n = 0
    while True:
        yield n
        n += step


g = step_gen(5)
print(next(g))
print(next(g))
print(next(g))
