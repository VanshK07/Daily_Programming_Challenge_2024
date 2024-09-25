import math

def find_lcm(n, m):
    return abs(n * m) // math.gcd(n, m)

N = int(input("Enter the first number: "))
M = int(input("Enter the second number: "))

lcm_value = find_lcm(N, M)

print(f"The Least Common Multiple of {N} and {M} is: {lcm_value}")
