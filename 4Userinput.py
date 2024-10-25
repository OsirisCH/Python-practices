# input (): is a function that prompts you to enter data in the result pannel, the function will 
# return the data as a string when you run the program
name = input("What is your name?: ")
age = input("How old are you?: ")
number_siblings = input ("Do you have siblings?: ")

age = int(age)
age = age + 1
print(f"Hello {name}!")
print(f"You are {age} years old")
print (f"You have {number_siblings} siblings")

