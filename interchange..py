def swap(lst):
    n = len(lst)
    if n % 2 == 0 and n >= 2:
        mid1 = n // 2 - 1
        mid2 = n // 2
        lst[mid1], lst[mid2] = lst[mid2], lst[mid1]
    return lst
print(swap([10, 20, 30, 40]))
print(swap([1, 2, 3, 4, ]))
print(swap(['a', 'b', 'c', 'd']))



# Interchange the particular element
def interchange(list1):
    m = int(input())
    n = int(input())
    list1[m-1], list1[n-1] = list1[n-1], list1[m-1]
    return list1
list1=[1,2,3,4,5,6,7,8,9]
print(interchange(list1))



# Interchange the next element
def change(list2):
    j = 2
    for i in range(1, len(list2), 2):
        if len(list2) % 2 != 0:
            list2[i - 1], list2[j - 1] = list2[j - 1], list2[i - 1]
            j += 2
    return list2
list2 =[10,20,30,40,50]
print(change(list2))


