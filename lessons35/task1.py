# def greeting(name, msg):
# 	print(f'{msg}, {name}!')

# lst = ['Sergey', 'Good evening']

# greeting(*lst)


# greeting('Sergey', 'Hello', 'Hi')

# def greeting(name='Sergey', msg='Hello'):
# 	print(f'{msg}, {name}!')

# dct = {'name': 'Michael', 'msg': 'Hi'}
# greeting(**dct)

# greeting('Michael', 'Hello')
# greeting()
# greeting(msg='Good morning')

# def greeting(*tlp):
# 	for name in tlp:
# 		print(f'Hello, {name}!')

# greeting('Sergey', 'Michael', 'Ivan')
# greeting('Sergey')
# greeting()


# todo: написать функцию args_rhombus считающую площадь ромба
# Считая, что площадь ромба равна половине произведения диагоналей:
# S = d1 * d2 / 2
# принимающую два позиционных аргумента d1 и d2

# def args_rhombus(d1, d2):
#     print(d1 * d2 / 2)


#
#
# args_rhombus(10, 10)

# todo: написать функцию kwargs_rhombus считающую площадь ромба
# Считая, что площадь ромба равна половине произведения диагоналей:
# S = d1 * d2 / 2
# принимающую два именованных аргумента d1 и d2

# def args_rhombus(d1=10, d2=10):
#     print(d1 * d2 / 2)
#
#
# args_rhombus(d2=20)

# todo: вызвать функцию args_rhombus с распаковкой списка
# в качестве аргументов

# lst = [5, 20]

# args_rhombus(*lst)


# todo: вызвать функцию kwargs_rhombus с распаковкой словаря
# в качестве аргументов
# dct = {'d1': 4, 'd2': 2}
#
#
# args_rhombus(**dct)

# Эту можно не делать:
# todo: написать функцию rhombus с не фиксированным кол-вом аргументов
# с аргументом в виде распаковки списка *lst
# где d1 это lst[0] а d2 это lst[1]

def rhombus(*lst):
    # d1 = lst[0]
    # d2 = lst[1]
    print(lst[0] * lst[1] / 2)


rhombus(20, 10)
