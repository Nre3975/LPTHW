import os
from sys import argv 

script, filename = argv # pylint: disable=unbalanced-tuple-unpacking 


print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

input("?")

print("Opening the file...") 
# Open file in write mode instead of the default read mode. 
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate() #Not really needed: using 'w' an existing file with the same name will be erased.

print("Now I'm going to ask you to write three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("Close and save the file.")
target.close()