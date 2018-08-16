# Given an array of integers, return a new array such that each element at index i of the new array is 
# the product of all the numbers in the original array except the one at i.


def products(nums):
    
    ascending_totals = []
    for num in nums:
        if ascending_totals:
            ascending_totals.append(ascending_totals[-1] * num)
        else:
            ascending_totals.append(num)
            
    descending_totals = []
    for num in reversed(nums):
        if descending_totals:
            descending_totals.append(descending_totals[-1] * num)
        else:
            descending_totals.append(num)
            
    descending_totals = list(reversed(descending_totals))
    
    result = []
    
    for i in range(len(nums)):
        if i == 0:
            result.append(descending_totals[i+1])
        elif i == len(nums) - 1:
            result.append(ascending_totals[i-1])
        else:
            result.append(ascending_totals[i-1] * descending_totals[i+1])
            
    return result


# two arrays are generated, one is the accumulator of the product of the integers of the array
# in ascending order and the other is the reverse. if i = 0 then we let the descending array
# accumulate down the array and take the value at i+1. if i is len(arr) - 1 we take the i-1
# value of the ascending array. any middle values can be found by multiplying the products
# on either side of i. if i is any value in the array not first or last we multiply ascending[i-1
# by descending[i+1] to find our total