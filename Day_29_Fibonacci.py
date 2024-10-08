def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    fib = [0] * (n + 1)
    
    # Base cases
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

n = 5
print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")
