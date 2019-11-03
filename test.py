def outer(x):
    def inner():
        return '戴了inner牌帽子的 ' + x()+'\n'

    return inner

@outer
def func() -> object:
    return '函数func'

print(func())
