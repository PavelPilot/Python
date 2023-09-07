def check(f):
    def result(x):
        r = f(x)
        if type(r) != int:
            raise Exception('Проверьте тип данных')

        return r
    return(result)

@check
def square(x):
    return x

print(square(5))

