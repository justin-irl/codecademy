# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.


#Write your function here
def divisible_by_ten(nums):
  y = 0
  for x in nums:
    if x % 10 == 0:
       y += 1
  return y

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))