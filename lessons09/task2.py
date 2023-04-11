"""Напишите функцию key_or_value(dct), принимающую в себя словарь(аргумент dct),
ожидающую от пользователя число 1 или 0. В зависмости от введённого числа функция
должна вывести в консоль ключи(если 1) или значения(если 0)"""

def key_or_value(dct):
    num = int(input())
    if num == 1:
        for key in dct.keys():
            print(key)
    elif num == 0:
        for value in dct.values():
            print(value)



sities = {
	'Moscow': 'Russia',
	'Tallin': 'Estonia',
	'Washington': 'Amerika',
	'Amsterdam': 'Nederlands'
}

key_or_value(sities)

# .keys() #возвращает ключи в словаре
# .values() возвращает значения в словаре
