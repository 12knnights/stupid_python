# ex6.py
# Defining variables
x = "There are 10 types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Printing the variables
print(x)  # Print the first string
print(y)  # Print the second string

# Printing formatted strings
print(f"I said: {x}")  # Using f-string to include variable x
print(f"I also said: '{y}'")  # Using f-string to include variable y

# Defining a boolean variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Printing the joke evaluation with the boolean variable
print(joke_evaluation.format(hilarious))  # Using format to insert the boolean value

# Defining two more strings
w = "This is the left side of..."
e = "a string with a right side."

# Concatenating strings
print(w + e)  # Concatenating and printing the two strings
