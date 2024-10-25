# Convert C° to F° or Kelvin, and the inverse
temperature = float(input("Enter the temperature: "))
unit = input("Celsius, Farenheit or Kelvin? (C°, F° or K°): ")
conversion = input("Enter unit to transform the temperature to: ")
if unit == "C°" and conversion == "F°":
    print(f"The temperature is {round ((temperature * 1.8) + 32, 2)} F°")
elif unit == "C°" and conversion == "K°":
    print(f"The temperature is {round (temperature + 273.15, 2)} K°")
if unit == "F°" and conversion == "C°":
    print(f"The temperature is {round ((temperature - 32) / 1.8, 2)} F°")
elif unit == "F°" and conversion == "K°":
    print(f"The temperature is {round ((temperature - 273) + 32, 2)} K°")
if unit == "K°" and conversion == "C°":
    print(f"The temperature is {round ((temperature -273.15), 2)} C°")
elif unit == "K°" and conversion == "F°":
    print(f"The temperature is {round ((temperature - 273.15) * 1.8 + 32, 2)} F°")
else:
    print("Invalid conversion unity")