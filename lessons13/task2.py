"""По данному натуральном nn вычислите сумму 1!+2!+3!+…+n!.
В решении этой задачи можно использовать только один цикл."""

n = int(input())
result = 1
factorial = 0
for num in range(1, n + 1):
    result *= num
    factorial += result
print(factorial)
