# Exercise 15: Reading Files. 

# Import argv from the sys library. 
from sys import argv 

# Unpack argv into script and filename vars. 
script, filename = argv # pylint: disable=unbalanced-tuple-unpacking 

#Return file object, store in txt var. 
txt = open(filename)

print(f"Here's your file: {filename}")
print(txt.read()) #Txt...Read your read command, no params.  
txt.close()

print ("Type the file name again:", end=' ')
# Get input, display the message "> "
file_again = input("> " ) 

# Open a new file, and print it out with read again. 
txt_again = open(file_again)
print(txt_again.read())
txt_again.close() git 


                    
