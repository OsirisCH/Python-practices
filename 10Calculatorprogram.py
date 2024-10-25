# Design a python calculator. 
# It is always better to work with float numbers with math operations.
operator = input("Enter an operator (+ - * /): ")
number1 = float(input("Enter the first number: "))
number2= float(input("Enter the second number: "))
# To define a character with a symbol, put "=="
if operator == "+":
    result = number1 + number2 
    print(result)
# The number 3 is for the quantity of decimal numbers that you want to add.
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1 * number2
    print(result)
elif operator == "/":
    result = number1 / number2
    print(round (result))
else:
    print(f"The inserted {operator} is not valid")

# If you want to round the division, for example, you must add round({number1 / number2})
# Since this is a calculator, it is not necesary to put a whole statement when printing the solution, just in case.
if operator == "+":
    print(f"The sum of the numbers is = {number1 + number2}")
elif operator == "-":
    print(f"The substraction of the numbers is = {number1 - number2}")
elif operator == "*":
    print(f"The mutiplication of the numbers is = {number1 * number2}")
elif operator == "/":
    print(f"The division of the numbers is = {number1 / number2}")