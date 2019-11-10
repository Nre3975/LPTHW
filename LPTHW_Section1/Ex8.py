# Variable consisting of 4 placeholders, currently just a string. 
formatter = "{} {} {} {}"
print(formatter)

# Print the variable, using the format function to fill the 4 placeholders. 
# Must fill all 4 placeholders. 
print(formatter.format(1,2,3,4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(True, False, 1, "Two"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your", 
    "Own Text Here", 
    "Maybe A poem", 
    "Or a song about fear"
))