"""Напишите функцию get_camel_case(str) принимающую текст в snake_case
и возвращаюшую его в CamelCase. Используйте тебличку методов строк а затем
методов списков."""

def get_camel_case(s):
    s = s.split('_')
    count = 0
    while count != len(s):
        s[count] = s[count].capitalize()
        count = count + 1

    print("".join(s))


get_camel_case('get_camel_case')






 # snake = "".join(["_" + c.lower() if c.isupper() else c for c in S])
#     return snake[1:] if snake.startswith("_") else snake
# a = 'ThisIsACamelCaseString'
# b = [i for i, e in enumerate(a) if e.isupper()] + [len(a)]
# c = [a[x: y] for x, y in zip(b, b[1:])]
# final = ['(Empty)']*10
# for i, case in enumerate(c):
#     final[i] = case
