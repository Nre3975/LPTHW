# Attempt to get script to 1 line. 

from sys import argv 
script, from_file, to_file = argv # pylint: disable=unbalanced-tuple-unpacking 

print(f"Copying data from {from_file} to {to_file}")

# Copy code. 
with open(from_file, "r") as f2:
    with open(to_file, "w") as f: f.write(f2.read())

print("Successful Copy.")

