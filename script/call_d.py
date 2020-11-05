# 实现装饰器

def decolate(func):
    x = 1

    def fun():
        print(x + 1)
        func()
        return fun

    return fun


@decolate
def test():
    print("结果")


#
# ttest = test()
# print(ttest)


# 通过装饰器实现单例模式
def single(self):
    instance = {}

    def func(*args, **kwargs):
        if func in instance:
            return instance[func]
        else:
            instance[func] = func(*args, **kwargs)
            return instance[func]

    return func


# 类实现装饰器
class delcote():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("装饰器1")
        return self.func()


@delcote
def testt():
    print("xxxxxx")
    return 2


t = testt()
print(t)
