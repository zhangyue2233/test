def fib(n):
    result = []
    a , b = 0 , 1
    while b < n:
        result.append(b)
        a , b = b , a+b
    return result    

def sayHi(name):
    print('hi %s' % name)    
