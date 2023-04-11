"Модифицировать функцию сinderella чтобы она возвращала один список по заданному типу."
# test_lst = [True, 1, 1.7, [True, 'hi'], 'python', False, .5]

# >>>cinderella(test_lst, bool)
# ...[True, False]

# >>>cinderella(test_lst, float)
# ...[1.7, .5]

test_lst = [True, 1, 1.7, [True, 'hi'], 'python', False, .5, {'key': 'value'}]

def cinderella(lst, tp):
    unilst = []
    for value in lst:
        if isinstance(value, tp):
            unilst.append(value)
    return unilst


print(cinderella(test_lst, dict))