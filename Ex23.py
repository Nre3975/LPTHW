# Import whole sys library. 
import sys  
# Because argv not imported specifically, need to qualify it when unpacking. 
script, encoding, error = sys.argv #pylint: disable=unbalanced-tuple-unpacking

# Function to: 
def main(language_file, encoding, errors): 
    line = language_file.readline()
    if line: 
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")    

main(languages, encoding, error)

# UTF-8, UTF-16, BIG5 etc. are codecs for encoding characters. 

print("\n\nProving Binary 1011010 is 90, and Ascii 90 = Z. ")
print("Number 90 in Binary: 0b1011010 = ", 0b1011010)
print("Confirm Ascii value for Z: ord('Z') = ", ord('Z'))
print("Show the character as Ascii value 90: chr(90) = ", chr(90))