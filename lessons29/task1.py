# 1) sys.argv from functools

# 2) reduce from functools

# 3)count, cycle from itertools

# 4)list compressions

from sys import argv

path, *args = argv
print(sum(map(int, [1, 2, 6])))
