# Ex10: What was that? 

# \ for excape characters. 
# Escape single or double quotes: 
print("I am 6'2\" tall")
print('I am 6\'2" tall')
print("""I am 6'2" tall""")

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"
line_cat = "I'm a \a\a\a cat" 
hex_cat = "I'm a \xAA cat"

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t* catnip\n\t* Grass 
"""

fat_cat2 = '''
I'll do a list: 
\t* Cat food
\t* Fishies
\t* catnip\n\t* Grass 
'''

formatter = "{} {} {}"

print(tabby_cat)
print(persian_cat)
print(backslash_cat) 
print(fat_cat)
print(fat_cat2)
print(hex_cat)

print(formatter.format(tabby_cat, line_cat, backslash_cat))

# \\ = Backslash. 
# \' = Single Quote. 
# \" = Double Quote. 
# \a = ASCII bell (BEL)
# \b = ASCII backspace (BS)
# \f = ASCII Formfeed (FF)
# \n = ASCII linefeed (LF) 
# \N = Character Named Name in the Unicode database (Unicode Only)
# \r = Carriage Return (CR)
# \t = Horizontal Tab (TAB)
# \uxxxx = Character with 32-bit hex value xxxx
# \uxxxxxxxx = Character with 32-bit hex value xxxxxxxx
# \v = ASCII vertical tab (VT) 
# \ooo = Character with octal value 000 
# \xhh = Character with hex value hh. 

