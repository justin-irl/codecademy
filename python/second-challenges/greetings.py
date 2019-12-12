# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

""" def add_greetings(names):
    lst = []
    i = 0
    name = names[i]
    for x in names:
        i += 1
        lst.append("Hello, " + name)
        return lst """

""" def test(names):
    for x in names:
        return "Hello, " + x

print(test(["Owen", "Max", "Sophie"])) """

def add_greetings(names):
  return ["Hello, " + names[i] for i in range(len(names)) ]

print(add_greetings(["Owen", "Max", "Sophie"]))


# did not self solve