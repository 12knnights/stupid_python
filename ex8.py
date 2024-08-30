# ex8.py

# Prompting the user for input
tuplemater = "{},{},{},{}"
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(tuplemater.format(1, 2, 3, 4))
x = tuplemater.format(1, 2, 3, 4)
print(formatter.format(x, x, x, x))
