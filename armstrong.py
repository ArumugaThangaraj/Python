# Find ArmStrong Number Program
a=int(input("Enter a number:"))
b=str(abs(a))
Sum=0
for i in range(0,len(b)):
    c=int(b[i])
    d=c**len(b)
    Sum+=d
if Sum==abs(a):
    print("The given number is ArmStrong number",Sum)
else:
    print("The given number is not a ArmStrong number",Sum)