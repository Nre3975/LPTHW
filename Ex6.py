# Exercise 6: Strings and Text. 

types_of_people = 10 

# String with variable inside it. 
x = f"There are {types_of_people} types of people"

# Two variables: Binary, Do_not. 
binary = "binary"
do_not = "don't"

# String containing words and the 2 variables inside the strong, Strings within strings. 
y =  f"Those who know {binary} and those who {do_not}."

# Print the two variables of strings. 
print(x)
print(y)

# String and a variable String within it 
print(f"I said {x}")
print(f"I also said: '{y}'")

# Boolean variable. 
hilarious = False 

# String, containing a space for a variable at the end. 
joke_evolution = "Isn't that joke so funny?! {}"

# .format string instead of f string, with the result of the boolean inserted. 
print(joke_evolution.format(hilarious))

# Two variables, then printed. 
w = "This is the left side of ..."
e = "a string with a right side."
print(w + e)