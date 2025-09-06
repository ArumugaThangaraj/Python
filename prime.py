 # Find Prime Number Program
import math
def isPrime(n):
    sqrt = math.floor(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return n

number = int(input("Enter a number: "))
if isPrime(number):
    print("Prime Number")
else:
    print("Composite Number")


