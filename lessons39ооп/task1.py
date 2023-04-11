class Worker:
    def __init__(self, position, salary, name):
        self.position = position
        self.salary = salary
        self.name = name

    def get_position(self):
        print(self.position)

    def get_salary(self):
        return self.salary


# Yurii = Worker('Developer', 50000, 'Юрий')
# Jobs = Worker('Boss', 100000000, 'Стив')


# Yurii.get_position() # get_position(Yurii)
# Yurii.get_salary()

class Company:
    def __init__(self, *workers):
        self.workers = workers

    def get_workers(self):
        for worker in self.workers:
            print(worker.name)

    def get_positions(self):
        for worker in self.workers:
            print(worker.name, ":", worker.position)

    def get_paying_fund(self):
        result = 0
        for worker in self.workers:
            result += worker.get_salary()
        print(result)


# apple = Company(Yurii, Yurii, Yurii, Jobs)
# apple.get_workers()
# apple.get_positions()
# apple.get_paying_fund()


# Yurii.name = 'Юрий'
# print(Yurii.name)


# todo: описать класс Dog
# в конструктор принять name и weight
# сделать их статическими атрибутами
# описать методы barking и running
# оба метода принимают int - количество повторений

class Dog:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def barking(self, n):
        for _ in range(n):
            print('гав')

    def running(self, n):
        for _ in range(n):
            print('*')


dog = Dog('toby', 70)
print(dog.name)
print(dog.weight)
dog.barking(5)
dog.running(10)