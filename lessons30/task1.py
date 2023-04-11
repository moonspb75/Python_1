def s(a, b):
    return a * b


def v(s, h):
    return s * h


def main(v):
    print(f'требуется {v} метров куб')


S = s(5, 4)
V = v(S, 2)
# main(V)

# main(v(s(5, 4), 2))
# s = (a + b) / 2 * h формула трапеции

# def trapezoid(a, b, h):
#     print((a + b) / 2 * h)
#
#
# trapezoid(2, 3, 2)

def trapezoid():
    a = int(input())
    b = int(input())
    h = int(input())
    return (a + b) / 2 * h


print(trapezoid())

# t = trapezoid()
# print(t)


# реализовать crud для управления интеренет-магазином





