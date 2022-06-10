src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def my_set(*args):
    res = set()
    for i in args:
        if not i in res:
            res.add(i)
        else:
            res.remove(i)
    return [x for x in args if x in res]


s = my_set(*src)
print(s)