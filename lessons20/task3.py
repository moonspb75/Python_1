"Получить от пользователя список чисел типа int. Вывести результат в консоль."

# user = int(input())
# user = list(input())
# for ix, num in enumerate(user):
#     user[ix] = int(num)
#
# print(user)

# user = input().split(', ')
# for ix, num in enumerate(user):
#     user[ix] = int(num)
#
# print(user)
user = list(map(float, input().split(', ')))


print(user)