def rstar(n):
    for row in range(0,n):
        for col in range(0,n):
            if row ==0 or col==(n-1) or row==col or col==0 or row==(n-1):
                print("*",end=" ")
            else:
                print(end="  ")
        print()
n=int(input("Enter a number: "))
rstar(n)
