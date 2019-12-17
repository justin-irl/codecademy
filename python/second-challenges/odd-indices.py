"""Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2]."""

def odd_indices(lst):
    new_lst = []
    count = 0
    while count < len(lst):
        for index in range(1, len(lst), 2):
            new_lst.append(lst[index])
            count += 1
        return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

# semi self solved, though I remembered the indentation issues from before where it prevented iterating over the full list

"""
def odd_indices(lst):
    new_lst = []
    count = 0
    while count < len(lst):
        for index in range(1, len(lst), 2):
            new_lst.append(lst[index])
            count += 1
            return new_lst

justins-MacBook-Pro:second-challenges justin$ python odd-indices.py
[3]

Then, the fixed version works:

justins-MacBook-Pro:second-challenges justin$ python odd-indices.py
[3, 10, -2]

"""
