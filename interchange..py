def swap(lst):
    n = len(lst)
    if n % 2 == 0 and n >= 2:
        mid1 = n // 2 - 1
        mid2 = n // 2
        lst[mid1], lst[mid2] = lst[mid2], lst[mid1]
    return lst
print(swap([10, 20, 30, 40]))
print(swap([1, 2, 3, 4, 5]))
print(swap(['a', 'b', 'c', 'd']))
