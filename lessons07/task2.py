"""Напишите функцию chess_queen(x_start, y_start, x_end, y_end), которая получает
на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала
для первой клетки, потом для второй клетки. Функция должна вернуть True, если из первой
клетки ходом королевы(ферзя) можно попасть во вторую или False в противном случае."""

def chess_queen(x_start, y_start, x_end, y_end):
    if abs(x_start - x_end) == abs(y_start - y_end) or x_start == x_end or y_start == y_end:
        return True
    else:
        return False
print(chess_queen(5, 2, 5, 8))



# if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')