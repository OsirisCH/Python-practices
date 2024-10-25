# Indexing allows to access elements or characters of a sequence using [] which is the indexng operator [start : end : step].
# Allows to create an starting point on the string, an end, or a step.
creditcardnum = "4827-2957-1400-2833"
print(creditcardnum[0])
print(creditcardnum[10])

# For example, to access the first 4 digits of the given string:
print(creditcardnum[0:4])
print(creditcardnum[5:9])
print(creditcardnum[::3])
print(f"XXXX-XXXX-XXXX-{creditcardnum[-4:]}")

# To reverse a string:
print(creditcardnum[::-1])