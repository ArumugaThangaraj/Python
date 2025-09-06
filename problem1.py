# Problem 1 Palindrom
def fun1():
    a = input("Enter Your String::")
    a = a.lower()
    b = a[::-1].lower().replace(" ", "")
    print(b)
    if a == b:
        print("Palindrome")
    else:
        print("Not Palindrome")


# Problem 2 remove any character from string
def fun2():
    n = input("Enter Your Character::")
    a = "Desert Eagle"
    b = ""
    for i in a:
        if i.lower() != n.lower():
            b += i
    print(b)


# Problem 3 Find the character and their count from a string
def fun3():
    a = "Night is dark and full of terror!"
    a = a.lower()
    b = {}
    for i in a:
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1
    for char in sorted(b):
        print(f"{char}: {b[char]}")


# Problem 4 Find a longest word in given string
def fun4():
    a = input("Enter Your String:")
    a = a.split(" ")
    longest = ""
    for i in a:
        if len(i) >= len(longest):
            longest = i
    print(f"Longest substring: {longest} and length: {len(longest)}")

# Problem 5 Reverse a string
def fun5():
    a = input("Enter Your String:")
    print(a[::-1])

# Problem 6 Reverse a words
def fun6():
    a = input("Write a paragraph..")
    a=a.split(" ")
    reversed = a[::-1]
    b=""
    for i in reversed:
        b+=i+' '
    print(b)


print("Select which option you want:")
print("1. Find Palindrome")
print("2. Remove Character from a string")
print("3. Count the Character from a string")
print("4. Find longest word")
print("5. Reverse the string")
print("6. Reverse the words")
selection = int(input("Select option: "))
if selection == 1:
    fun1()
elif selection == 2:
    fun2()
elif selection == 3:
    fun3()
elif selection == 4:
    fun4()
elif selection == 5:
    fun5()
elif selection == 6:
    fun6()
