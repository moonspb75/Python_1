# todo: Необходимо создать класс Ingredient,
# конструктор класса принимает три обязательных аргумента:

# name - название ингредиента
# weight - вес в граммах
# cost - стоимость в рублях
# В класс Ingredient необходимо добавить следующие getter-методы:

# get_name() - возвращает название ингредиента
# get_weight() - возвращает вес в граммах
# get_cost() - возвращает стоимость в рублях

class Ingredient:
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def get_name(self):  # возвращает название ингредиента
        return self.name

    def get_weight(self):  # возвращает вес в граммах
        return self.weight

    def get_cost(self):  # возвращает стоимость в рублях
        return self.cost * (self.weight / 100)


cream_sauce = Ingredient('Сливочный соус', 50, 50)
blue_cheese = Ingredient('Сыр блю чиз', 100, 100)
mozzarella = Ingredient('Моцарелла', 100, 100)
cheddar = Ingredient('Чеддер', 100, 100)
parmesan = Ingredient('Пармезан', 100, 100)
pepperoni = Ingredient('Пепперони', 100, 200)


# todo: Необхоидмо создать класс Pizza,
# конструктор класса принимает один обязательный аргумент
# name - название пиццы.

# Необходимо добавить в класс следующие методы:

# get_name() - возвращает название пиццы
# add_ingredient(ingredient) - принимает объект типа Ingredient и добавляет ингредиент в пиццу
# get_cost() - возвращает стоимость пиццы в рублях
# get_weight() - возвращает вес пиццы в килограммах (1кг=1000г)

class Pizza:
    def __init__(self, name):
        self.name = name  # pizza.name = 'Четыре сыра'
        self.ingredients = []

    def get_name(self):  # - возвращает название пиццы
        return self.name

    def get_cost(self):  # - возвращает стоимость пиццы в рублях
        # return sum(ingredient.get_cost for ingredient in self.ingredients)
        result = 0
        for ingredient in self.ingredients:
            result += ingredient.get_cost()
        return result

    def get_weight(self):  # - возвращает вес пиццы в килограммах (1кг=1000г)
        result = 0
        for ingredient in self.ingredients:
            result += ingredient.get_weight()
        return result

    def add_ingredient(self, ingredient):  # - принимает объект типа Ingredient и добавляет ингредиент в пиццу
        self.ingredients.append(ingredient)


pizza_fc = Pizza('Четыре сыра')
pizza_pp = Pizza('Пепперони')

pizza_fc.add_ingredient(cream_sauce)  # add_ingredient(pizza, cream_sauce)
pizza_fc.add_ingredient(blue_cheese)
pizza_fc.add_ingredient(mozzarella)
pizza_fc.add_ingredient(cheddar)
pizza_fc.add_ingredient(parmesan)

pizza_pp.add_ingredient(mozzarella)
pizza_pp.add_ingredient(cheddar)
pizza_pp.add_ingredient(parmesan)
pizza_pp.add_ingredient(pepperoni)


# print(pizza_fc.get_cost())
# print(pizza_fc.get_weight())


# todo: Необходимо создать класс Order и добавить в него следующие методы:

# add_pizza(pizza) - принимает объект типа Pizza и добавляет пиццу в заказ
# get_cost() - возвращает стоимость заказа в рублях
# print_receipt() - печатает чек на экран, пример вывода чека на экран:

# Четыре сыра (0.450кг) - 450.00руб
# Ветчина и сыр (1.000кг) - 600.00руб
# Мясная (0.550кг) - 445.00руб
# Обратите внимание, что вес выводится с 3 знаками после запятой,
# а стоимость с 2 знаками после запятой,
# количество знаков перед запятой может быть любым. Воспользуйтесь форматированием строк в вашем ЯП.
class Order:
    def __init__(self):
        self.pizza_lst = []

    def add_pizza(self, pizza):  # - принимает объект типа Pizza и добавляет пиццу в заказ
        self.pizza_lst.append(pizza)

    def get_cost(self):  # - возвращает стоимость заказа в рублях
        result = 0
        for pizza in self.pizza_lst:
            result += pizza.get_cost()
        return result

    def print_receipt(self):  # - печатает чек на экран, пример вывода чека на экран:
        for pizza in self.pizza_lst:
            print(f'{pizza.get_name()} ({pizza.get_cost()}) - {pizza.get_weight()}руб')


order = Order()
order.add_pizza(pizza_fc)
order.add_pizza(pizza_pp)

order.print_receipt()
