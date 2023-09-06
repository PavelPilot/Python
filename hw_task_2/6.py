def check(f):
    def result(x):
        r = f(x)

    try:
        x.type = int
    except:
        print('Тип данных не целочисленный')
    return r
return(result)

@check
def square(x):
    return x ** 2


print(square(5))

