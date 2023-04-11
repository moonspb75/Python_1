# todo: повторить термины

# класс
# атрибут - переменная привязанная к экземпляру --> экзепляр.атрибут
# метод - функция првязанная к экзепляру --> экзепляр.метод()
# конструктор __init__  --> экземпляр = Класс()
# экзмпляр
# ссылка на экземпляр

class Tree:
    def __init__(self, lenght):
        self.lenght = lenght  # oak.lenght = 10

    def get_lenght(self):
        return self.lenght

    def set_lenght(self, lenght):  # экземпляр.метод() --> метод(экземпляр)
        print(f'дерево меняется на {lenght} метров')
        self.lenght = lenght


# oak = Tree(10)

# print(oak.lenght)
# oak.set_lenght(11)


# todo: 1)определить класс Drug содержащий один атрибут weight без конструктора.
# class Drug:
# 	weight = 10

# phentonil = Drug()

# print(f'{phentonil.weight=}')
# print(f'{Drug.weight=}')

# todo: 2)определить класс Drug создающий один атрибут weight через конструктор.
# class Drug:
# 	def __init__(self, weight):
# 		self.weight = weight

# mig = Drug(5)

# print(f'{mig.weight=}')

# todo: 3)определить класс Drug
# создающий один атрибут через конструктор.
# и getter-метод возвращающий этот атрибут.
# class Drug:
# 	def __init__(self, weight):
# 		self.weight = weight

# 	def get_weight(self):
# 		return self.weight

# cetrin = Drug(3)
# print(f'{cetrin.get_weight()=}')


# todo: 4)определить класс Drug
# создающий один атрибут через конструктор.
# и setter-метод устанвливающий этот атрибут.

class Drug:
    def __init__(self, weight):
        """

        :type weight: object
        """
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        print(f'Содержание меняется на {weight} мг')
        self.weight = weight


enup = Drug(2.5)
print(f'{enup.get_weight()=}')
enup.set_weight(2)
