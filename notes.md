Fibonacci sequence

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

F(0) = 0
F(1) = 1
f(n) = F(n-1) + f(n-2)


def fib(n):
    cache = {}

def fib_inner(n):
    nonlocal cache

    if n == 0:
        return 0

    if n == 1:
        return 1

    if not n in cache:
    cache[n] = fib_inner(n-1) + fib_inner(n-2)
    
    return cache[n]

    #if it's not in the cache
        cache[n] == fib(n-1) + fib(n-2)
    
    #return cache[n]

    return fib_inner(n)