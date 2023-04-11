# 0 1 1 2 3 5 8 13 21

def fib(n):
    firstn = 0
    result = 0
    secondn = 1
    if n == 0:
        pass
    elif n == 1:
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
