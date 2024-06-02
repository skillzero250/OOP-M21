import builtins


def my_print(*args, **kwargs):
    builtins.print(*(arg.upper() for arg in args))


print = my_print
print('Нельзя ли потише?')