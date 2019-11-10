import sys  
script, encoding, error = sys.argv #pylint: disable=unbalanced-tuple-unpacking

# Main Function: Reads line from file, if the line exists 
# call print_line function, then call main again which will 
# now have the seek location at the next line start. 
def main(language_file, encoding, errors): 
    line = language_file.readline()
    if line: 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# Encodes each line. 
# Strip strips the \n from the end of the line. 
# encode language from the file and encode into raw bytes. 
# decode to get string too, print both.
def print_line(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.decode(encoding, errors=errors)
    raw_bytes = cooked_string.encode(encoding, errors=errors)
    print(cooked_string, "<===>", raw_bytes)

# Open languages file. 
languages = open("languages.txt", "rb") #Open in Binary mode. 

main(languages, encoding, error)
