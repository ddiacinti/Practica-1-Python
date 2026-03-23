import random

categorias = {
    "programacion": ["python","programa","variable","funcion",
                    "bucle",  ] ,
    "tipos_de_datos" :["cadena","entero","lista",]}

print ("Categorias disponibles: ")
for categoria in categorias: 
    print(categoria)
categoria_elegida = input("Elegi una categoria: ")

word = random.choice(categorias[categoria_elegida])
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

puntaje = 0

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje = puntaje + 6
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if len(letter) > 1 or not ("a" <= letter <= "z" or "A" <= letter <= "Z"):
        print("Entrada no válida")
        continue 
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje = puntaje - 1
        print("Esa letra no está en la palabra.")

    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0

print (f"Tu puntaje fue de: {puntaje}")