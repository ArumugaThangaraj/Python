# Using Built-in function
import math
n = int(input())
print(math.factorial(n))

# Using loop
n = int(input("Enter a number: "))
fact =1
for i in range(n,0,-1):
    fact = fact * i
print(fact)

#Using recursive function
def fun(n):
    if n==0:
        return 1
    else:
        return n*fun(n-1)
n = int(input("Enter a number: "))
print(fun(n))
