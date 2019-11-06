#Exercise 19: Functions and Variables

#Define function with 2 inputs. 
def cheese_and_crackers(cheese_count, boxes_of_crackers): 
    print(f"You have {cheese_count} cheeses")
    print(f"You  have {boxes_of_crackers} boxes of crackers")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket.\n")

# Call function with numbers.
print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

# Call function with variables.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call function with Maths
print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

# Call function with variables and math. 
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Define simple additional function. 
def oneplustwo(int1, int2):
    return(int1 + int2) 

var1 = 10
var2 = 5
var3 = 2
var4 = 1

print(oneplustwo(1, 1))
print(oneplustwo(-10, -21))
print(oneplustwo(10-10+3, 10))
print(oneplustwo(5 + 5, 1 + var3))
print(oneplustwo(var1, var2))
print(oneplustwo(var1 + 10, var1))
print(oneplustwo(var1 / var3, 10))
print(oneplustwo(var3 - var1 * var1, var2))
print(oneplustwo(-13, var4))
print(oneplustwo(int(input('Number to add: ')), var2))