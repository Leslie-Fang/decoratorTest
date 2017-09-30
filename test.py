import decorator as decorator


def test1():
    print("This is test1")
    return 1

@decorator.logger
def test2():
    print("This is test2")
    return 1

@decorator.logger2()
def test3():
    print("This is test3")
    return 1

@decorator.logger2()
def test4(first,second):
    '''
    :param first: the first input params
    :param second: the second input params
    :return:
    '''
    print("This is test4")
    return first+second

if __name__ == '__main__':
    print(test1)
    print(test1())
    #test2 print is decorator function
    print(test2)
    print(test2())
    #test3 differs with test2
    #test3 print still is test3 function
    print(test3)
    print(test3())

    print(test4)
    print(test4.__doc__)
    print(test4(1,2))