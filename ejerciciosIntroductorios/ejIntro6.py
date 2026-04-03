#6. Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
#una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
#finalizar.

multiplos = []
otros =[]
n = int(input("INGRESA UN NUMERO: "))
for n in range (1, n+1): 
    if n % 5 == 0:
     multiplos.append(n)
    else:
     otros.append(n)
print (multiplos)
print(otros)