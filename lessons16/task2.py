"""Домашняя работа"""
"""Напишите функцию new_line(start, stop, step=2) которая печатает
числа от start до stop с шагом увеличивающимся на 1 каждый раз  
Например:

>>>line(0, 15)
...0         0 + 0 = 0 #0 + 0
...3         3 + 1 = 4 #2 + 1
...6         6 + 2 = 8 #4 + 2
...9         9 + 3 = 9 #6 + 3
...          12 + 4  12 #8 + 4 

"""

def new_line(start, stop, step=2):
    for i in range(start, stop, step):
        print(i)

new_line(0, 10)
