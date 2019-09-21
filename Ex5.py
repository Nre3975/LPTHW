# Exercise 5: More Variables and Printing. 

Name = 'NRE3975'
age = 32 #Not a lie. 
height = 70 # Inches. 
heightcm = height * 2.54 
weight = 190 #lbs
weightkg = weight * 0.4535
eyes = 'blue'
teeth = 'white'
hair = 'brown'



print(f"Let''s talk about {name}.")
print(f"He''s {height} inches tall.")
print(f"he''s {weight} pounds heavy")
print("Actually, that''s not too heavy")
print(f"He''s got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on coffee")

total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")

print(f"Weight in cm {heightcm}, weight in KG {round(weightkg)}")
