#Create a function called append_size that has one parameter named lst.

#The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

#For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.

def append_size(lst):
    size = len(lst)
    lst.append(size)

    return lst

print(append_size([23, 42, 108]))

# solved correctly! 
# worth noting when trying to return variable
    # new_lst = list.append(size)
    #returned: none

# 'append will return None if it worked. There is not much more to it than that.'