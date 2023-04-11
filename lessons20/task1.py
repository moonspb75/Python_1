# todo: Создать словарь
# dct = {'key': 'value', 'key1': ['lst_value', 'lst_value1']}

# todo: Обратиться к значению в словаре
# >>>dct['key']
# ...value

# todo: Обратиться к элементу списка внутри словаря
# >>>dct['key1'][1]
# ...lst_value1

# todo: Присвоить новое значание в словарь
# >>>dct['new_key'] = 'new_value'
# >>>dct['new_key']
# ...new_value

# todo: Отосортировать список по типу данных

lst = [1, 2.1, 2, 2.2, 3, 2.3]


def cinderella(lst, tp=int):
    intlst = []
    floatlst = []
    for num in lst:
        if isinstance(num, tp):
            intlst.append(num)
        else:
            floatlst.append(num)

    print(intlst, floatlst)


cinderella(lst, int)
