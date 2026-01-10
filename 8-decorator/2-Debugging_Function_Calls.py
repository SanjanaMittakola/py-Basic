#Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        argvalue =', '.join(str(arg) for arg in args)
        kwargvalue =', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling {func.__name__} with args : {argvalue} and kwargs : {kwargvalue}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")

greet("sanju",greeting="oyee")





#def debug(func):
#    def wrapper():
#        return func()
#   return wrapper

#def hello():
#    print("hello")
#hello()


