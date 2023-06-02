# Fibonacci with iterative procedure concept from SICP

def fib_iter(a,b, count):
    if count == 0:
        
        return b
    else:
        return fib_iter(a+b,a,count -1)

def fib(n):
    return fib_iter(1,0,n)
    
print(fib(7))

