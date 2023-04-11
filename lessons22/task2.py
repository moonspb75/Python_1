# При решении ориентироваться на таблицу методов строк.
"""Напишите функцию get_camel_case(str) принимающую текст в snake_case
и возвращаюшую его в CamelCase. Используйте тебличку методов строк а затем
методов списков
Пример вызова:

# >>>get_camel_case('snake_case')
# ...'SnakeCase'
#
# >>>get_camel_case('auto_increment')
# ...'AutoIncrement'"""


def get_camel_case(str):
    str = str.split('_')
    # count = 0
    # while count != len(str):
    #     str[count] = str[count].capitalize()
    #     count = count + 1

    for ix, word in enumerate(str):
        # str[ix] = str[ix].capitalize()
        str[ix] = word.capitalize()

    print("".join(str))


get_camel_case('snake_case')
