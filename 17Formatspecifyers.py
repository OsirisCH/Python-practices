# The format specifyers give format to a value depending of the flags inserted in the code.
price1 = 25.7423
price2 = -28.5382
price3 = 2929.67
print(f"Price 1 is ${price1:2.f}") # To display only 2 decimal places
print(f"Price 2 is ${price2:10}") # To make the values to have 10 spaces or a certain number or spaces before 
print(f"Price 3 is ${price3:015}") # To make the values have 00000 displayed before the spaces designed
print(f"Price 1 is ${price1:<10}") # To left justify a value
print(f"Price 2 is ${price2:>10}") # To right justify a value
print(f"Price 3 is ${price3:^10}") # To center values
print(f"Price 1 is ${price1: }") # To insert an aditional space 
print(f"Price 2 is ${price2:+5}") # To give a positive sign before, but if the value is negative, it wil continue being negative
print(f"Price 3 is ${price3:,}") # To put commas that assign bigger numbers