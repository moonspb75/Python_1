# lst_sum(lst)
# todo: написать  функцию, печатающую сумму чисел до n.
# n как аргумент.

def sum_range(n):
    resalt = 0
    for i in range(n + 1):
        resalt += i
    print(resalt)


sum_range(5) # 15