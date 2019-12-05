# Create a function called middle_element that has one parameter named lst.

#If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

# if lst is odd, we should get the middle number. eg len(lst) == 5, return lst[2]
# if lst is even, we should get the two middle numbers. eg len(lst) == 6, return lst[2, 3] and avg them ((2+3)/2)

def middle_element(lst):
    middle = len(lst)

    if middle % 2 != 0:
        return "odd"
    else:
        return "even"
    
print(middle_element([5, 2, -10, -4, 4, 5]))

list = [5, 2, -10, -4, 4, 5]

print(len(list))
#print(int(len(list)/2))
#print(int(len(list)/2) - 1)