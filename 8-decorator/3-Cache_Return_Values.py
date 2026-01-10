#Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
import time 

def cache(func):
    cachevalue = {}
    print(cachevalue)
    def wrapper(*args):
        if args in cachevalue:
            return cachevalue[args]
        return func(*args)
    return wrapper


@cache
def longrun(a,b):
    time.sleep(2)
    return a + b

print(longrun(2,3))
print(longrun(12,13))