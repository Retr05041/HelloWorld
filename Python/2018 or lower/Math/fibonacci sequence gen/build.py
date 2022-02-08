# chaches number
fibonacci_chache = {}

def fibonacci(n):

    # looks at chache
    if n in fibonacci_chache:
        return fibonacci_chache[n]

    # errors
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise TypeError("n must be a positive int")

    # fibonacci sequence
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # saves last number to the cache
    fibonacci_chache[n] = value
    return value

# loops throught n times and prints fibonacci sequence for each
for n in range(1, 1000001):
    print(n, ":", fibonacci(n))
