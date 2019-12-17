"""
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
"""

"""
def larger_sum(lst1, lst2):
    a = sum(lst1)
    b = sum(lst2)
    if a > b:
        return lst1
    return lst2
"""

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for x in lst1:
        sum1 += x
    for y in lst2:
        sum2 += y
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))
#tests on lines 31, 21
print(larger_sum([4, 3, 9], [10, 3, 7]))
print(larger_sum([1, 9], [1, 7]))
print(larger_sum([2, 4], [3, 3]))

# self solved, original code commented out, lesson doesn't accept the sum() command, re-written with loops