def fib(n):
    a,b=0,1
    while n>0:
        a,b=b,a+b
        n=n-1
    print(a)
num=int(input("Enter a number: "))
fib(num)

# Find Fibonacci using Recursive function
# def recurse(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return recurse(n-1)+recurse(n-2)
# num=int(input("Enter a number: "))
# print(num,"the number is",recurse(num))