class Calculator:
    type_c = "Bughalter"

    def my_sum(self, a, b):
        print(a + b)

    def my_sub(self, a, b):
        print(a - b)

    def my_multyply(self, a, b):
        print(a * b)

    def my_division(self, a, b):
        print(a // b)


my_calc = Calculator()


# my_calc.my_multyply(5, 6) #my_multyply(my_calc, )
# my_calc.my_division(6, 3)
# print(my_calc.type_c)

class Person:
    def __init__(self, age, is_developer):
        self.age = age  # me.age
        self.is_developer = is_developer
        print(self.age, self.is_developer)

    def coding(self):
        print('hello world')

    def teaching(self):
        print('Do this right!')


me = Person(25, True)
he = Person(30, False)
# me.coding()
# me.teaching()
# print(me.age, me.is_developer)

she = Person(34, False)
# print(type(she))

# Переменная - атрибут
# Функция - метод

# class - общая структура объединяющая
# поведение и информацию

# атрибуты - статические, динамические
