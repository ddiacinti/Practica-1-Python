cantSegundos = int (input (f"INTRODUCI UNA CANTIDAD DE SEGUNDOS: "))
enHora = cantSegundos // 3600
sobrantes = cantSegundos % 3600
enMinutos = sobrantes // 60
enSegundos = sobrantes % 60
print (f"LA CANTIDAD DE HORAS QUE EQUIVALE SON {enHora}")
print (f"LA CANTIDAD DE MINUTOS QUE EQUIVALE SON {enMinutos}")
print (f"LA CANTIDAD DE SEGUNDOS QUE EQUIVALE SON {enSegundos}")
