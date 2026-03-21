#Crea un programa que dado un número N ingresado por el usuario, imprima los
#números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue Entrega
#donde haga falta
# cuando haces  = es asignacion, == es comparacion
n = int(input("INGRESA UN NUMERO: "))
for n in range (1, n+1): 
    if n % 5 == 0:
     print (n)
    