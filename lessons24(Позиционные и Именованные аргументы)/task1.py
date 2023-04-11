def function():
    print("i'm function")


# function()

def greeting(name, greet):  # Позиционные аргументы: name, greet
    print(f'{name} {greet}')


# greeting('Sergey', 'Hello')

def grt(name='Sergey', greet='Hello'):  # Именованные аргументы: name, greet
    print(f'{name} {greet}')

# grt(greet='Good morning')
