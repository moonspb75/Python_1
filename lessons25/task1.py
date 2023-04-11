def hello():
    print('hello')


# hello()

def hello1(greet, name):
    print(f'{greet}, {name}!')


# hello1('Good evening', 'Sergey')


def hello2(name, greet='hello'):
    print(f'{greet}, {name}!')


# hello2("Sergey")
# hello2("Sergey", 'Good evening')


def hello3(name="Sergey", greet='hello'):
    print(f'{greet}, {name}!')


# hello3()

def hello4(*arg):
    name, greet, *others = arg
    print(f'{greet}, {name}! {others}')


args = ["Sergey", 'hello']


# hello4(*args)
# hello4("Sergey", 'hello', 'How is your day?')


def thesourse(*arg):
    dct = {}
    for person in arg:
        key = person[0]  # Ключ, первая буква

        if key in dct:
            dct[key].append(person)
        else:
            dct[key] = [person]
    print(dct)


"""4. * (вместо задачи 3)
Написать
функцию
thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
dct = {
    "А": {"П": ["Петр Алексеев"]},
    "С": {"И": ["Иван Сергеев", "Инна Серова"], "А": ["Анна Савельева"]}
}
"""


def thesaurus_adv(*arg):
    ext_dct = {}

    for person in arg:
        inner_dct = {}
        firstname, lastname = person.split()
        ext_key = lastname[0]
        inner_key = firstname[0]
        # print(ext_key, inner_key, person)

        if inner_key in inner_dct:
            inner_dct[inner_key].append(person)
        else:
            inner_dct[inner_key] = [person]

        if ext_key in ext_dct:
            if inner_key in ext_dct[ext_key]:
                ext_dct[ext_key][inner_key].append(person)
            else:
                ext_dct[ext_key][inner_key] = [person]
        else:
            ext_dct[ext_key] = inner_dct

    print(ext_dct)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# print(dct)

# lst = []


# thesourse("Катерина", "Николай", "Мария", "Илья", "Иван")
# thesourse(*lst)


# def thesourse_adv(*args):
#     ext_dct = {}
#     dct = {}
#     print(thesourse(*args))


# for person in args:
# 	firstname, lastname = person.split()
# 	if lastname[0] in ext_dct:
# 		pass
# 	else:
# 		dct[lastname[0]] =
#
# thesourse_adv("Катерина Николаева", "Николай Петров", "Мария Мишкина")
#
# {
#     'К': ['Катерина Николаева'],
#     'Н': ['Николай Петров'],
#     'М': ['Мария Мишкина']
# }
#
# {
#     'Н': {'К': ['Катерина Николаева']},
#     'П': {'Н': ['Николай Петров']},
#     'М': {'М': ['Мария Мишкина']}
# }
