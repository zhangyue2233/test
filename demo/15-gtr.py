# a generator function which returns the Fibonacci series 
def fib():
    a,b =1,1
    while True:
        yield a
        a,b = b , a+b
    pass #this is a null statement which does nothing when executed, useful as a placeholder.

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break