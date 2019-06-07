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


----

Scratch pad for eating_cookies

Can minus by 1, 2, or 3

Count the number of times we can get to zero by minus-ing a chain of either 1, 2 or 3

So for example 5:

1) 3 - 2 = 0
2) 2 - 3 = 0
3) 3 - 1 - 1 = 0
4) 1 - 3 - 1 = 0
5) 1 - 1 - 3 = 0
6) 2 - 2 - 1 = 0
7) 1 - 2 - 1 = 0
8) 1 - 1 - 2 = 0
9) 2 - 1 - 1 - 1 = 0
10) 1 - 2 - 1 - 1 = 0
11) 1 - 1 - 2 - 1 = 0
12) 1 - 1 - 1 - 2 = 0
13) 1 - 1 - 1 - 1 - 1 = 0
