friends = 2

# Adding: works the same between variables
friends = friends + 5
friends += 2 #To short the expression
print(friends)

# Substraction
friends -=2
print(friends)

# Multiplication
friends *=3
print(friends)

# Division
friends /=2
print(friends)
# To get the remainder of any division, a % must be placed
remainder = friends % 2
print(remainder)

# Exponents - friends = friends **2 (long version)
friends **=2
print(friends)
# In the math module (import math) the exponents must be expressed with a pow(number, elevated to-number)