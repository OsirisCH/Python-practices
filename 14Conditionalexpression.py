# A conditinal expression refers to a one-line shortcut for the if-else statements (ternary operators). It prints
# or assign one of the values based on a condition X, if the condition else Y.
num = int(input("Insert a number: "))
# print("X" if the condition else "Y") - This is the general structure
print("Positive" if num > 0 else "Negative")    
result = "Even" if num % 2 == 0 else "Odd"
print(result)

a = int(input("Insert a number: "))
b = int(input("Insert a number: "))
max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age = int(input("Insert your age: "))
status = age if age >= 21 else "Underage"
print(status)

temp = int(input("Insert the temperature: "))
weather = "It's hot" if temp >= 25 else "Nice weather"
print(weather)

access = input("Enter your user role: ")
access_level = "Full access" if access == "admin" else "Limited access"
print(access_level)