"""# Методы
# todo: как использовать методы
variable_name.name_function()

# Методы строк:

# todo: как разбить строку на список по пробелу # string.split()
>> > 'hello, how are you?'.split()
...['hello,', 'how', 'are', 'you?']
# todo: как разбить строку на список по литере 'o'
>> > 'hello, how are you?'.split('o')
...['hell', ', h', 'w are y', 'u?']
# todo: как разбить строку на список по символу '_'
>> > 'hello,_how_are_you?'.split('_')
...['hello,', 'how', 'are', 'you?']

# todo: как найти индекс символа/сочетания символов #string.find()
>> > 'hello'.find('e')
...1
>> > 'hello'.find('l')
...2  # если искомых символов много, то возвращается индекс первого

# todo: как заменить символы в строке #string.replace()
>> > 'hello'.replace('lo', 'p')
...
'help'
# todo: как заменить слова в тексте
>> > 'i love you'.replace('love', 'hate')
...
'i hate you'
# string.count()


# todo: как проверить символ на заглавность #string.istitle()
>> > 'T'.istitle()
...
True
>> > 't'.istitle()
...
False

# Методы списков:

# todo: как присоединить новое значение в список # lst.append()
>> > lst = [1, 2, 3]
>> > lst.append(12)
>> > lst
...[1, 2, 3, 12]
# todo: как добавить кортеж в конец списка
>> > lst.append((1, 3, 5))
>> > lst.append((1, 3, 5))
>> > lst
...[1, 2, 3, 12, (1, 3, 5), (1, 3, 5)]

# todo: как склеить список строк через разделитель
# "separator".join(iterable_list)

>> > "!".join(['hello,', 'how', 'are', 'you?'])
...
'hello,!how!are!you?'

>> > "_".join(['hello,', 'how', 'are', 'you?'])
...
'hello,_how_are_you?'

>> > " hi ".join(['hello,', 'how', 'are', 'you?'])
...
'hello, hi how hi are hi you?'

>> > f"{3 * 4}".join(['hello,', 'how', 'are', 'you?'])
...
'hello,12how12are12you?'"""
