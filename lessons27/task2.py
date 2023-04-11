def get_count():
    n = int(input())
    dct = {}

    for _ in range(n):
        lst = input().split()
        for words in lst:
            if words in dct:
                dct[words] += 1
            else:
                dct[words] = 1
    return dct


max_occ = 0
max_word = ''

for word, occ in get_count().items():
    if max_occ < occ:
        max_occ = occ
        max_word = word

print(f'Самое встречаемое слово: {max_word}')
print(f'его встречаемость: {max_occ}')
