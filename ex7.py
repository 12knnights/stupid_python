# ex7.py
# Asking for user input
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# Defining a multi-line string
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Printing the poem
print("--------------")
print(poem)
print("--------------")

# Defining variables
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# Defining more variables
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Starting point
start_point = 10000
jars, beans, crates = secret_formula(start_point)

# Printing results
print(f"With a starting point of: {start_point}")
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
