# ex13.py

# Defining a function that takes parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

# Calling the function with direct numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Calling the function using variables
print("OR, we can use variables from our script:")
amount_of_cheese = 15
amount_of_crackers = 25
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling the function using math
print("We can even do math inside too:")
cheese_and_crackers(10 + 5, 20 + 10)

# Calling the function using variables and math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 5, amount_of_crackers + 5)