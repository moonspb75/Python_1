# todo: описать класс Car с атрибутом wheels - количеством колёс

class Car:
    def __init__(self, wheels=4):
        self.wheels = wheels


# todo: создать экземпляр этого класса
niva = Car(wheels=4)


# todo: вывести атрибут wheels через экземпляр этого класса

# print(niva.wheels)


# todo: описать класс Party с атрибутом guests - количеством гостей
# celebration принимает кол-во бутылок и увеличевает  атрибут bottles

class Party:
    def __init__(self, guests): # self-это всегда переменная для экземпляра(birthday)
        self.guests = guests    # атрибут, это переменная(self.guests)
        self.bottles = 0

    def celebration(self, n): # setter
        self.bottles += n

    def get_bottles(self):  # метод, это функция
        return self.bottles / self.guests, 'на человека'


# todo: создать экземпляр этого класса
birthday = Party(10)

# print(birthday.bottles)
birthday.celebration(10)
# print(birthday.bottles)
# print(birthday.bottles)
# print(birthday.get_bottles())


# todo: описать класс Yacht с атрибутом crue - количеством экипажа
class Yacht:
    def __init__(self, crue, speed):
        self.crue = crue
        self.speed = speed
        self.path = 0

    def walking(self, m): # setter
        self.path += m

    def path_time(self):
        return f'{self.path / self.speed} часа'

# todo: создать экземпляр этого класса
santer = Yacht(5, 40)

# todo: вывести атрибут guests через экземпляр этого класса
# print(santer.crue)
print(santer.path)
santer.walking(100)
print(santer.path)

print(santer.path_time())
santer.high = 9
print(santer.__dict__)
