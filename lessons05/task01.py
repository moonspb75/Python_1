"""Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
Даны две различные клетки шахматной доски, определите, может ли король попасть с первой
клетки на вторую одним ходом. Функция king(x_start, y_start, x_stop, y_stop) получает
на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала
для первой клетки, потом для второй клетки. Функция должна вернуть True, если из первой
клетки ходом короля можно попасть во вторую или False в противном случае."""


def king(x_start, y_start, x_stop, y_stop):
    if abs(x_start - x_stop) == 1 or abs(y_start - y_stop) == 1:
        return True
    else:
        return False


print(king(1, 2, 3, 2))

#     if abs(x1 - x2) == abs(y1 - y2):
#      print("True")
#     else:
#      print("False")
#
# chess_bishop(1, 2, 3, 5)

#     if abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
#         return True
#     elif abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
#         return True
#     else:
#         return False
#
#
# print(chess_horse(2, 1, 4, 2))
