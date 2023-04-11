def sum():
    a = int(input())
    d = int(input())
    print(a + d)

def sum1(a, d):
    print(a + d)

def sum2(a=1, b=4):
    print(a + b)

def sym3(a=5, b=7):
    return a + b
# sum()

# sum1(1, 2)

# sum2(1, 2)
# sum2(3)
# sum2()

# a = sym3()
# print(a)

print(sym3() * 2)
