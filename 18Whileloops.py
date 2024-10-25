# A while loop will execute some code WHILE some condition remains true.
name = input("Insert your name: ")
while name == "":                         # "" is an empty string
    print("You did not enter your name")
    name = input("Insert your name: ")
print(f"Hello {name}")     # The execution of the code could potentially continue forever, so it is important to give a condition 
# that prevent that to happens, but it must be correctrly vinculated to the while section.

age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be a negative number")
    age = int(input("Enter your age: "))
print(f"You are {age} years old") 

food = input("Enter a food you like: ")
while not food == "q":
    food = input("Enter another food you like (q to quit): ")
print("Bye!")

number = int(input("Enter a # between 1 and 10: "))
while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input("Enter a # between 1 and 10: "))
print(f"{number} is correct")