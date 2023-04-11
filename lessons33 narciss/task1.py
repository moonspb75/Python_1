# Create a function named divisors/Divisors that takes an integer n > 1
# and returns an array with all of the integer's divisors(except for 1
# and the number itself), from smallest to largest. If the number is
# prime return the string '(integer) is prime'

# Example:
# divisors(12); #should return [2,3,4,6]

def divisors(integer):
    lst = []
    for i in range(2, integer):
        if integer % i == 0:
            lst.append(i)
    if lst:
        return lst
    else:
        return f'{integer} is prime'


# print(divisors(7)); #should return [2,3,4,6]
# divisors(13); #should return "13 is prime"
# divisors(25); #should return [5]


def f_hi(name):
    print(f'Hello, {name}!')


# f_hi('Sergey')

def narcissistic(value):
    l = len(str(value))
    result = 0
    for number in str(value):
        result += int(number) ** l
    print(value == result)


# narcissistic(73)

# 1) получить каждую цифру и возвести в степень
# 2) сложить всё это
# 3) сравнить value == result


def fib(n):
    firstn = 0
    secondn = 1

    result = 0

    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        for num in range(n - 2):
            result = firstn + secondn
            firstn = secondn
            secondn = result

        print(result)


for i in range(1, 10):
    fib(i)


def f(n):
    f1 = 0
