from sys import argv 
from os.path import exists #Returns true if a file exists. 
script, from_file, to_file = argv # pylint: disable=unbalanced-tuple-unpacking 

print(f"Copying data from {from_file} to {to_file}")

# Next two lines could be combined into one. 
in_file = open(from_file)
indata = in_file.read() 

print(f"The input file is {len(indata)} bytes long") 
print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, or CTRL-C to abort.")

input("> ")

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close() 