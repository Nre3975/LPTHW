from sys import argv 
scriptname, filename = argv # pylint: disable=unbalanced-tuple-unpacking
 
target_file = open(filename, 'r')
print(target_file.read())
target_file.close()
