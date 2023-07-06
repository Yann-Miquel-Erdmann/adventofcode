def func2(a):
    a = a[:]
    a[0]+=1
    print(a)


def func1(a):
    func2(a)
    func2(a)

func1([1])