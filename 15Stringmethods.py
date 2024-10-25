# The first function is related to the LENGHT - len(X), it gives the lenght of a string variable in an integer number.
# The spaces count into the lenght, not only the letters.
name = input("Enter your name: ")
result = (len(name))
print(f"The lenght of your name is {result} characters")

# The X.find(Y) function will return the position of a given character, for example, spaces, in the text. The count starts
# by zero, not one. SPA - Cuenta desde la posición donde el caracter está en el texto, NO REFIERE A LA CANTIDAD DE ESPACIOS O A
# LA CANTIDAD DEL CARACTER INSERTADO 
result2 = name.find("a") #There's a space here
print(result2)

#The opposite function is X.rfind(Y), it is a reverse search. For example, if the name Ana Garcia has 9 characters including 
# space, and you search for an a, the function will return the number 9. SPA - el resultado será la posición del caracter 
# solicitado contando desde el final, pero la posición será la misma en la longitud del String. 
result3 = name.rfind("a")
print(result3)

# If you search a character that is not in the string, the result would be a -1.

# The X.capitalize(Y) capitalizes the first letter on a string.
capname = name.capitalize("name")
print(capname)

# The X.upper(Y) capitalizes all the letters on a string.
uppname = name.upper(name)
print(uppname)

# The X.lower(Y) put all the characters in lowercases.
# Is also a boolean method for testing a string. 
lowname = name.lower(name)
print(lowname)

# If a string contains digits, the boolean function X.isdigit(Y) will return TRUE only if it contains digts and FALSE in 
# the other cases
digname = name.isdigit(name)
print(digname)

# The X.isalpha(Y) is also boolean. It returns TRUE only if all the characters are digits and FALSE in the opposite case or 
# if it is an space in the string.
alhpaname = name.isalpha(name) # Test the expression X.isalnum(Y) for strings that had a character different from its original format
print(alhpaname)

# The X.replace("Y", "Z") replaces a given character with another, is more useful with numbers in a string character, or even to
# eliminate some character with an empty string "".
phnumber = input("Enter your phone: ")
phone_num = phnumber.replace("+39","")
print(phone_num)

# EXERCISE - Validate user input. It has to be no more than 12 characters, without any spaces or digits.
username = input("Enter a new username: ")
if len(username) > 12:
    print("Your username cannot be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain any spaces")
elif not username.isalpha():
    print("Username cannot contain any digits")
else:
    print(f"Welcome {username}!")