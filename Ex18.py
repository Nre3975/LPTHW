# Exercise 18: Names, Variables, Code, Functions. 

# Def used to state defining function, followed by it's name 
# then arguments, then a colon. Subsequent lines are indented. 
def print_two(*args): #*args: Take all args into function as a list for unpacking. 
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2 {arg2}")

def print_two_again(arg1, arg2): 
    print(f"arg1: {arg1}, arg2 {arg2}")

def print_one(arg1): 
    print(f"arg1: {arg1}")

def print_none(): 
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

### Function Checks. 
# Starts with Def. 
# Name only has Chars and _
# Arguments inside () after function name. 
# Arguments have unique names within the funciton namespace. 
# Indent lines of code. 
# 