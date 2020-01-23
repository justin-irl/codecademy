"""
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

`same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])`
"""

# to find the matching numbers
# check an index in lst1 against the range if indexes in lst2
# if it matches one, add it to a new empty list
# eg: lst[0] checks against lst2[1, 2, 3, etc], then lst[1] checks against lst2[1, 2, 3, etc]


def same_values(lst1, lst2):
    new_lst = []
    for x in range(len(lst1)):
        if lst1[x] == lst2[x]:
            new_lst.append(x)
    return new_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# solved