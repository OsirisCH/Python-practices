# Create a program to see how much money you will have after a certain amount of years.
principle = 0
rate = 0
time = 0

while True: 
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:       #The while loop continues forever if you don´t break it whith this or a print(something)
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate  can't be less than or equal to zero")
    else:
        break

while True: 
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break

# Compound interest formula:
total = principle * pow((1+rate/100), time)
print(f"The balance after {time} year/s: $ {total:.2f}")

# The while created can use boolean conditions, because in this case, the while is false, you need to enter more than zero to 
# obtain a result. SPA - Las tres condiciones de la calculadora son falsas, por ello pueden usarse booleanos para definir el 
# loop. Pero se coloca un else - break al final, para evitar que el loop siga. El uso de este formato dependerá del ejercicio dado.