# Create a function called middle_element that has one parameter named lst.

#If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

# if lst is odd, we should get the middle number. eg len(lst) == 5, return lst[2]
# if lst is even, we should get the two middle numbers. eg len(lst) == 6, return lst[2, 3] and avg them ((2+3)/2)

#my attempt
def middle_element(lst):
    length = len(lst)
    middle = length // 2
    even = (lst[middle - 1] + lst[middle]) / 2

    if middle % 2 == 0:
        return lst[middle]
    else:
        return even

print(middle_element([5, 2, -10, -4, 4, 5]))

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4]))

# didn't pass but don't know why