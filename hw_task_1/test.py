def print_result(f):
    def result(x):
        r = f(x)
        print(f'Результат вычислений: {r}')
        return r
    return result

@print_result
def square(x):
    return x**2

square(3)