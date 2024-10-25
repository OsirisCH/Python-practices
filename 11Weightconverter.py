# Convert pounds to Kg, and the inverse
weight = float(input("Enter your weight: "))
unit = input ("Kilograms or pounds? (Kg or Lb): ")
if unit == "Kg":
    print(f"You weight {round (weight * 2.2, 2)} Lb")
elif unit:
    print(f"You weight {round (weight / 2.2, 2)} Kg")
