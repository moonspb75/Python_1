"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""


''' решение list '''
seasons = ["Весна", "Лето", "Осень", "Зима"]
monthnumb = int(input("введите номер месяца: "))
if 3 <= monthnumb <= 5:
    print(seasons[0])
elif 6 <= monthnumb <= 8:
    print(seasons[1])
elif 9 <= monthnumb <= 11:
    print(seasons[2])
else:
    print(seasons[3])

''' решение dict'''

d = {"season1": "Зима", "season2": 'Весна', "season3": "Осень", "season4": "Лето"}
monthnumb = int(input("введите номер месяца: "))
if 3 <= monthnumb <= 5:
    print(d["season2"])
elif 6 <= monthnumb <= 8:
    print(d["season4"])
elif 9 <= monthnumb <= 11:
    print(d["season3"])
else:
    print(d["season1"])