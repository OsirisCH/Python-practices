# The statements are a short form of decision making, using the "If" and #Else". The code only does something if 
# some conditions are true.
# The command "elif" serves to check multiple conditions in a program if one condition is fake
#age = int(input("Enter your age: "))
if age >= 90:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
else: 
    print("You must be +18 to be signed up")
    
#ALWAYS put a : after the if: or the else:
# For the elif, it seems not necesary

response = input("Would you like food? (Yes/No): ")
if response == "Yes":
    print("Have some food")
else:
    print("No food for you")

name = input("Enter your name: ")
if name == "":
    print("You did not type your name")
else:
    print(f"Welcome, {name}!")

# With boolean variables, the result of this exercise will vary according if for_sale is True or False
for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

online = False
if online:
    print("The user is online")
else:
    print("The user is offline")