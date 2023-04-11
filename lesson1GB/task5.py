"""Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

# print ("введите выручку")
# viruchka = int(input())
# print ("введите издержку")
# izderzka = int(input())
# if viruchka > izderzka:
#     print ("прибыль")
#     rent = (viruchka-izderzka) / viruchka
#     print("рентабельность = "+ str(rent))
#     print("введите количество сотрудников")
#     sotrudniki = int(input())
#     rent = rent/sotrudniki
#     print("прибыль на сотрудника = " + str(rent))
# else:
#     print("убыток")

# Можно написать:
# izderzka = int(input("введите издержку"))
# Результат будет как у двух инструкций:
# print ("введите издержку")
# izderzka = int(input())
# в строке rent = rent/sotrudniki - ошибка
# rent - норма прибыли
# прибыль в расчете на сотрудника определяется по формуле:
# pribl_na_sotrudnika = (viruchka-izderzka) / sotridniki

proceeds = int(input())  #выручка
costs = int(input())   #издержки
profit = proceeds - costs #прибыль
if profit > 0:
    print(f'Прибыль: {profit}')
    print(f'Рент выручки: {profit / proceeds}')
    print(f'Прибыль фирмы в расчете на одного сотрудника: {proceeds / int(input("Введите количество сотр-ов: "))}')
elif profit < 0:
    print("Убыток")


