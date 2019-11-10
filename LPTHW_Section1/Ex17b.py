from sys import argv 
# With closing
with open(argv[1], "r") as f2: 
    with open(argv[2], "w") as f: f.write(f2.read())

# Without Closing. 
open(argv[2], "w").write(open(argv[1], "r").read())

