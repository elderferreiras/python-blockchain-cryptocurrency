def fun1(arg):
    print(f'arg: {arg}')


def fun2(*args):
    for arg in args:
        fun1(arg)


super_function = lambda *fun_args: fun2(*fun_args)

super_function(1, 2, 3, 4)
