# Создадим словарь столиц:
sities = {
	'Moscow': 'Russia',
	'Tallin': 'Estonia',
	'Washington': 'Amerika',
	'Amsterdam': 'Nederlands'
}
# Выведем его ключи в консоль с помощью метода .keys
# print(sities.keys())

# Так как мы получили список dict_keys(['Moscow', 'Tallin', 'Washington', 'Amsterdam'])
# его можно перебрать в цикле for:

for key in sities.keys():
	print(key)

# >>>Moscow
# >>>Tallin
# >>>Washington
# >>>Amsterdam

# Если вспомнить как осуществляется обращение к элементу по ключу,
# >>>sities['Amsterdam']
# То совместив это с циклом с 14-ой строки получим:
for key in sities.keys():
	print(key, sities[key])

# >>>Moscow Russia
# >>>Tallin Estonia
# >>>Washington Amerika
# >>>Amsterdam Nederlands

