""" Напишите функцию ОЖИДАЮЩУЮ от пользователя строку, а потом возврающую её в верхнем
регистре. Например "You are a grate coder!"  станет "YOU ARE A GRATE CODER!". """

def up():   #объявили функцию
    s = input()  #ожидаем строку
    return s.upper() #  возвращаем в вверхнем регисттре
print(up()) # печатаем вызов функции




# # s1 = input("")
# s2 = s1.upper() # метод строки повышающий регистр
# print(s2)