def two_sum(lst,num):
    seen = set()
    for i in range(len(lst)):
        if(num - lst[i] in seen):
            return True
        seen.add(lst[i])
    return False

# loop through list and check if value of target subtract current element exists in list,
# if not, add to set (which stops duplicates) and continue

from bisect import bisect_left

def two_sum(lst,num):
    lst.sort()
    for i in range(len(lst)):
        j = binary_search(lst, num - lst[i])
        if j == -1:
            continue
        elif j != i:
            return True
        elif (j+1) < len(lst) and lst[j+1] == num:
            return True
        elif (j-1) >= 0 and lst[j-1] == num:
            return True
        return False
        
def binary_search(lst,num):
    res = bisect_left(lst,num)
    if 0 <= res < len(lst) and lst[res] == num:
        return res
    return -1

# sort the list and begin a loop, take lst & target number subtract current element and 
# see if that number exists in the list by checking its theoretical bisection point of the list
# and seeing if its there. if it is there (and it isnt the same as i which would cause a problem with
# target of 20 and i @ 10 etc) then check if its not equal to i, in which case true, or if it
# is, then if theres another of the same left or right. if there is, then return true, false if not