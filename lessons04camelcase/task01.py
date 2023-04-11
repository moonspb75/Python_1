""
def fib(n):
    fib1 = 0
    fib2 = 1
    result = 0
    f = 0
    n = n - 2
    while f != n:
        result = fib1 + fib2
        fib1 = fib2
        fib2 = result
        f = f + 1
    return result



# count = 0
# while count != 4:
#     print(count)
#     count = count + 1
print(fib(6))