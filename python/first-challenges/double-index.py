# Create a function named double_index that has two parameters named lst and index.

# The function should return a new list where all elements are the same as in lst except for the element at index, which should be double the value of the element at index of lst.

# If index is not a valid index, the function should return the original list.

# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

# double_index([1, 2, 3, 4], 2)

# my attempt
#def double_index(lst, index):
 #   list_len = len(lst)

  #  if index < list_len:
   #     lst[index] = lst[index] * 2
    #    return lst
    #else:
     #   return lst

# one from forums
# def double_index(lst, index):
 #   if index < len(lst):
  #      lst[index] = lst[index] * 2
   # return lst

# provided solution
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst

print(double_index([3, 8, -10, 12], 2))

# did not self solve