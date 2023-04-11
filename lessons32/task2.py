# todo Факториалом числа n называется произведение 1 × 2 × ... × n.
# Обозначение: n!.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)


factorial(5)  # 24
