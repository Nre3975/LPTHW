# Import whole sys library. 
import sys  
# Because argv not imported specifically, need to qualify it when unpacking. 
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
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)

# Open languages file. 
languages = open("languages.txt", encoding="utf-8")    

# call the languages function with the open file, encoding type, and 
# error type (Strict, replace etc.)
main(languages, encoding, error)

# UTF-8, UTF-16, BIG5 etc. are codecs for encoding characters. 

print("\n\nProving Binary 1011010 is 90, and Ascii 90 = Z. ")
print("Number 90 in Binary: 0b1011010 = ", 0b1011010)
print("Confirm Ascii value for Z: ord('Z') = ", ord('Z'))
print("Show the character as Ascii value 90: chr(90) = ", chr(90))

# Print 
print(chr(72)+chr(101)+chr(108)+chr(108)+chr(111), chr(87)+chr(111)+chr(114)+chr(108)+chr(100))

# Disecting Code: 
raw_bytes_test = b'\xe6\x96\x87\xe8\xa8\x80'
utf_string_test = "文言"
print(raw_bytes_test.decode())
print(utf_string_test.encode())
print(raw_bytes_test == utf_string_test.encode())
print(utf_string_test.encode() == raw_bytes_test)

#NB: calling this with UTF-16 shows the difference: Whereas UTF-8 knows the standard chars
# as seen in b'Afrikaans' <===> Afrikaans, UTF-16 has to encode these as seen so: 
# b'\xff\xfeA\x00f\x00r\x00i\x00k\x00a\x00a\x00n\x00s\x00' <===> Afrikaans