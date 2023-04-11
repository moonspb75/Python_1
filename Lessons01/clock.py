minuts = int(input('Введите количество минут с начала суток: '))
hours = minuts // 60
minuts = minuts % 60
print(f"{hours} часов и {minuts} минут")
