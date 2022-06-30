def type_logger(func):

    def wrapper(*args):

        for arg in args:
            print(f'calc_cube({arg}: {type(arg)})')
            res = func(arg)

        return res

    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3

var = calc_cube(5, 3, 6)

print(var)
