"""
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums
"""

def max_num_no_loop(nums):
    return max(nums)

print(max_num_no_loop([50, -10, 0, 75, 20]))

# no need for a loop
# will try a loop though since that is what the lesson is asking for

# declare your function `max_num` with input `lst`
def max_num(lst):

    # set variable `biggest_number` which is equal to index 0 of lst
    biggest_number = lst[0]

    # do for each `nums` in the range, where the range is the length of lst
        # ah this is the key part I was missing, you have to include the range to tell the function to check each of the entries in the list and not just stop when it reaches the first one!!!
        # so in order to iterate over the entire list you have to tell it to: do this x times, where x is the length of the list provided!
    for nums in range(len(lst)):

        # if index `nums` of lst, is greater than, the variable of biggest number, which is set to `lst[0]` to begin with
        if lst[nums] > biggest_number:

            # then update the variable `biggest number` to equal `lst[nums]`
            biggest_number = lst[nums]
    
    # then return `biggest number`
    return biggest_number

print(max_num([50, -10, 0, 75, 20]))
print(max_num([100, 20, 34, 150]))