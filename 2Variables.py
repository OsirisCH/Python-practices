# Variables are containers for a value, they're designated with an equal = sign, all variables behaves as if 
# it was the value  it contains. 
# The variables are: string, integer, float, boolean.

# String variable: it is written quoted, but when it's inserted in the code, it is not to be quoted
#                  serie of characters that can be numbers, but numbers are characters too, 
#                  not specifically for math
first_name = "Lisa"
owner = "JC"
food = "meat" 
email = "lisacachorra@gmail.com"
print (first_name)

# To integrate the variable with another things, a letter f must go first to indicate the use of
# a variable, and a set of {} must contain the variable
print (f"Hello {first_name}")
print (f"You like {food}")
print (f"Your email is {email}")

# Integer: they only contain numbers, not for decimal numbers, use them for math expressions
age = 8
quantity = 10
num_of_people = 6
print (f"You are {age} years old")
print (f"You are buying {quantity} bags of {food}")
print (f"You have bitten {num_of_people} people")

# Float: a number that can contain a decimal portion written with a POINT, NOT A COMMA
priceone = 3.50
pricetwo = 5.00
print (f"Your {food} cost ${priceone} but you wanted the {food} that cost {pricetwo}")

# Boolean: a variable that is true or false, yes or no, two options and nothing more. Linked to IF statements
likes_bath = False
likes_park = True
has_lice = False
is_hairy = True
has_a_owner = True
print (f"Is it true that {first_name} likes baths?: {likes_bath}")
print (f"It is true that {first_name} likes walks?: {likes_park}")
if has_lice:
    print (f"Take {first_name} to the vet")
else:
    print (f"Give {first_name} dog cookies")
if is_hairy:
    print (f"{first_name} is a mammal")
else:
    print (f"{first_name} must be an impostor")
if has_a_owner:
    print (f"Of course {first_name} has a ownner, he is {owner}")
else:
    print (f"{first_name} must be a stray")