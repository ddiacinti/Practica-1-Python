#. Escribe un programa que simule una caja registradora: el usuario ingresa precios de
#productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
#acumulado. Nota: utilizá la sentencia break cuando haga falta.
total = 0
precio =-1
while precio != 0:
 precio = int(input('INGRESE UN PRECIO'))
 total = total + precio
print (f'EL PRECIO ACUMULADO ES: {total}')
