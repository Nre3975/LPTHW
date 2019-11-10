from sys import argv 
from os.path import exists #Returns true if a file exists. 
script, from_file, to_file = argv # pylint: disable=unbalanced-tuple-unpacking 

print(f"Copying data from {from_file} to {to_file}")

# Combining Lines. 
indata = open(from_file).read() 
out_file = open(to_file, "w").write(indata)
out_file.close()
indata.close() 

print("Successful Copy.")
