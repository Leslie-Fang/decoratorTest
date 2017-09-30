import functools

def logger(func):
    def decorator():
        print("Before {}",format(func))
        res = func()
        return res
    return decorator


## recommand use the this type of decorator
def logger2():
    def decorator(func):
        #when define the function, code in this block would be executed
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            #when call the function, code in this block would be execute
            print("Before {}", format(func))
            res = func(*args, **kwargs)
            print("After {}", format(func))
            return res
        return wrapper
    return decorator