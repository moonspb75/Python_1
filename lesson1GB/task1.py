"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк."""





duration = int(input())
hour = duration // 3600
min = duration % 3600 // 60
sec = duration % 3600 % 60

print(f' {hour:02}:{min:02}:{sec:02}')

# для вывода 2-х разрядов с лидирующими нулями можно использовать модификаторы:
# print(f"{hour:02}")
# тогда не придется делать проверки типа if hour < 10:
# между операциями надо ставить пробелы (так код лучше читается и это соответствует рекомендациям PEP8)
# вместо:
# minute=seconds//60
# писать:
# minute = seconds // 601