"""Шахматный слон ходит по диагонали. Даются две различные клетки шахматной
доски, напишите функцию chess_bishop(x1, y1, x2, y2),  определяющую
может ли слон попасть с первой клетки на вторую одним ходом. Результат
True/False функция возвращает"""
# from math import abs
def chess_bishop(x1, y1, x2, y2):

    if abs(x1 - x2) == abs(y1 - y2):
     print("True")
    else:
     print("False")

chess_bishop(1, 2, 3, 5)