# The logical operators OR, AND, NOT, are used for the evaluation of multiple conditions at the same time.
# OR = at least one condition must be true
temp = int(input("Enter the temperature: "))
is_raining = True
if temp > 35 or temp < 0 or is_raining :
    print("There will be no outdoor meeting")
else:
    print("The outdoor meeting is still scheduled")

# AND = both conditions must be true
is_sunny = True
if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny outside")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")

# NOT = inverts the condition, but it is better to use simple logic instead of this operator in order to avoid 
# mistakes.
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")