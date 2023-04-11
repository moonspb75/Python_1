""" Напишите функцию row(start, stop), выводящую список чисел
от start до stop"""
# range(start, stop, step)

def row(start, stop):
    for r in range(start, stop):
        print(r)

row(4, 9)