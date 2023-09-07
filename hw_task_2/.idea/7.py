def check(f):
    def result(x):
        r = f(x)
        try:
            if type(r) != int:
                raise Exception('Проверьте тип данных')
        except:
            f(x)


        return r
    return(result)

@check
def square(x):
    print('Вызов ф-ции')
    return x

print(square(5))
