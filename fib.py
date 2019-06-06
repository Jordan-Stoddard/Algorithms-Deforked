# This is the bottom up version of computing the fibonacci sequence. Time complexity: O(n) Space complexity: O(1)
def fib_bottom_up(n):
    if n == 0:
            return 0

    if n == 1:
        return 1
    
    pprev = 0
    prev = 1
    i = 1
    while i < n:
        pprev, prev = prev, prev + pprev
        i += 1
    
    return prev



# This is the top-down version of computing the fibonacci sequence. It is less ideal because the space complexity is O(n)
def fib(n):
    cache = {}  # Memoization

    def fib_inner(n): #O(n) time complexity
        nonlocal cache

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n not in cache:
            cache[n] = fib_inner(n-1) + fib_inner(n-2)

        return cache[n]

    return fib_inner(n)