'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
'''

def first_missing_positive(arr):
    if not arr:
        return 1
    s = set(arr)
    i = 1
    while i in s:
        i += 1
    return i

lst = [3, 4, -1, 1]

print(first_missing_positive(lst))
