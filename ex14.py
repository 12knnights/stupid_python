# ex14.py

# Defining a function that takes parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

# Prompting the user for input
print("Let's make some cheese and crackers!")
print("How many cheeses do you have?")
amount_of_cheese = int(input("> "))  # Convert input to integer

print("How many boxes of crackers do you have?")
amount_of_crackers = int(input("> "))  # Convert input to integer

# Calling the function with user input
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling the function with direct numbers
print("We can also call the function with direct numbers:")
cheese_and_crackers(10, 20)

# Calling the function using math
print("We can even do math inside too:")
cheese_and_crackers(5 + 5, 10 + 10)
