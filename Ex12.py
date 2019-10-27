# Exercise 12: Prompting People.
# Adding a prompt to the input request. 

age = input("How old are you? ")
height = input(f"Youre age is {age}? Thank you, how tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Input man page: python -m pydoc input: Read a string from standard input

# Open man page: Open a file in a defined mode. Return stream. File name is 
## either text of byte string, mode such as r for read, w for write etc. 

# OS: OS Routines for NT/Posix. os.path, os.name etc. Using os means program 
## has better chance of being portable between different platforms. 

# Sys: provides access to some variables used or maintained by the interpreter 
## and to functions that interact strongly with the interpreter. It is always available.