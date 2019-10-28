# Exercise 13: Parameters, Unpacking, Variables.  
# Write a script which accepts arguments. 
# argv: Argument variable. holds the arguments passed into the script at runtime. 
from sys import argv 

# Unpack argv into 4 variables.
#script, first, second, third = argv
#Less: script, arg1, arg2
scriptname, arg1, arg2, arg3, arg4 = argv

print("The script is called :", scriptname)
print("The first variable is called:", arg1)
print("The second variable is called:", arg2)
print("The third variable is called:", arg3)
print("The fourth variable is called:", arg4)

arg4 = input('Sorry, what did you say for \'arg4\'?')

print("Okay, The fourth variable is called:", arg4)