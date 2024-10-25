# A nested loop is a loop within another loop (outer, inner). The type doesn't matter as well as what is in which loop.
    # Outer loop looks like this
        # Inner loop looks like this

for X in range(3):                 # Whatever coded in this loop will be executed 3 times
    for Y in range(1, 10):         # The variable inside could not be the same of the first X
        print(Y, end = "")

# Print a rectangle
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")
for X in range(rows):
    for Y in range(columns):
        print(symbol, end="")
    print()

