# Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
#oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
#espacios. Las palabras cortas deben ser excluidas del resultado final

palabra = input('Ingresa una palabra, cuando termines apreta enter')
oracion = ' '
while palabra != ' ':
    if (len(palabra) > 3): 
     oracion = oracion + palabra + ' '
    palabra = input('Ingresa una palabra, cuando termines apreta enter')
print (f'oracion {oracion}')
