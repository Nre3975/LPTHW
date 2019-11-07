# Exercise 20: Functions and Files. 
from sys import argv 
script, input_file = argv # pylint: disable=unbalanced-tuple-unpacking 

# Function to print whole file. 
def print_all(f): 
    print(f.read().decode('UTF-8'))

# Rewind to position 0. 
# Seek() sets files position to the argument.
def rewind(f):
    f.seek(0)

# Custom positioning function, set the position in the file to char of choice. . 
def rewind2(f, offset):
    f.seek(offset)

# Actual rewind function: Rewind X characters from current location:
# The 2nd argument is the weence: 0 = Start of file, 1 = Current location 
# 2 = end of file, so this is set position relative to current location. 
# However this wont work unless file is opened in binary mode. Which in turn 
# means read needs to be decoded to work as intended. 
def rewind3(f, offset): 
    f.seek(offset, 1)

# Function to print line 'line_count' of file f. 
def print_a_line(line_count, f):
    print(line_count, f.readline().decode('UTF-8')) 

# Open file. 
current_file = open(input_file, 'rb') 

print("First let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape...")
rewind(current_file) 

print("Set file to location char 6:")
rewind2(current_file, 6)
print_a_line(1, current_file)

print("Rewind from char 10 (File is now at the end after running above line) to char 2.")
rewind3(current_file, -8)
print_a_line(1, current_file)

print("Seek location will now be the end of line 1.")
print_all(current_file)

print("Let's print three lines:")
rewind(current_file) 
for x in range(1, 4): 
    print_a_line(x, current_file)
    x+=1





