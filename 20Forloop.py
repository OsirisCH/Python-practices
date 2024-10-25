# A for loop is for executing a code a fixed number of times. You can itinerate over a range, string, sequence, etc. Contrary to a 
# while loop, this loop is not potentially infinite.

# SPA - Imagina que tienes una caja con pelotas de colores, y quieres sacar las pelotas una por una para mirarlas. 
# Un bucle for es como si le dieras instrucciones a alguien para que saque una pelota, la mire y luego saque la siguiente,
# hasta que no quede ninguna pelota en la caja. En programación, se usa el bucle for para repetir una acción varias veces, 
# como sacar todas las pelotas, o imprimir una letra de una palabra cada vez, o hacer algo con cada número en una lista.

#The basic syntax is this:
for X in range(1, 11):  # For example, to count until 10, it is necesary to stop before reaching 11, not at ten.
    print(X)
print("Hello person")

# SPA - Supongamos que quieres contar del 1 al 5. Con un bucle for, podrías escribirlo así:
for i in range(1, 6):
    print(i)
# for i in range(1, 6): Esto le dice al programa "Haz algo para cada número del 1 al 5." i es la variable que va cambiando,
# primero es 1, luego es 2, después 3, 4, y finalmente 5. 
# range(1, 6) significa "Empieza desde el 1 y sigue hasta el 5" (pero no incluye el número 6).
# print(i): Esto le dice al programa: "Imprime el valor de i en cada vuelta del bucle." El código imprimirá:
# 1
# 2
# 3 
# 4 
# 5

# Ahora, imagina que tienes la palabra "gato" y quieres ver cada letra una por una. Puedes usar un bucle for para hacerlo:
word = "gato"
for letter in word:     # "Para cada letra en la palabra gato, vamos a hacer algo."
    print(letter)       # Primero, la letter es "g", luego "a", después "t" y finalmente "o".

# If you are making a countdown:
for X in reversed(range(1, 11)): 
    print(X)
print("Happy new year!")
# Another example:
for i in range(5, 0, -1):
    print(i)

# If you want a count that goes in 2 by 2 (It is going to be for even numbers, since it starts with 1):
for X in range(1, 11, 2): 
    print(X)

# For strings: 
creditcardnum = "4827-2957-1400-2833"
for X in creditcardnum:
    print(X)

# If you want to skip a number:
for X in range(1, 21):
    if X == 13:
        continue        # If ypu write a BREAK, the counter will stop until 12.
    else:
        print(X)

# SPA - Si quisieras repetir una frase varias veces, el bucle for también es útil:
for i in range(3):
    print("I love Italy!")
# La salida será "I love Italy! 3 veces, en columna.

# EJERCICIO LAB 4 - Versión profesional - La palabra que vamos a cortar en pedacitos
word = "Football"
substrings = []     # Lista para guardar todas las subcadenas (pedacitos de la palabra)
for i in range(len(word)):  # Primer bucle: recorre cada letra de la palabra, de izquierda a derecha
        for j in range(i + 1, len(word) + 1):   # Segundo bucle: recorre desde la posición 'i' hasta el final de la palabra
               substrings.append(word[i:j])     # Corta la palabra desde 'i' hasta 'j' y guarda el pedacito
substrings.sort(key=len)        # Ordenamos las subcadenas por su longitud
for substring in substrings:    # Imprime todas las subcadenas ordenadas
    print(substring)

# Versión corta 
word = "Football"   # Esta es la palabra que vamos a recortar
for i in range(len(word)):      # Bucle externo: decide desde dónde empezamos a recortar
       for j in range(i + 1, len(word) + 1):     # Bucle interno: decide cuántas letras vamos a recortar desde 'i'
                print(word[i:j])      # Imprimimos la subcadena que va desde la posición 'i' hasta la 'j'