### Condicionales
'''
If -> condicion
Elif -> otra condicion
Else -> si no cumple nada 

La condicion compara el valor X con las diferentes condificones que le hemos dado.
Si el valor cumple la primer condicion se para. -> Ejecuta el IF
Si no cumple con la primera condicion, sigue a la 2 y asi sucesivamente. -> Ejecuta los ELIF
En caso de no cumplirse ninguna condicion- -> ejectua el ELSE

Ej:
Variable: tengo 29 años.
Condicion1 (if): tienes mas de 40 años.
Condicion2 (elif): tienes menos de 10 años.
No cumple condificones (Else): No tienes mas de 40 años ni menos de 10

años = 29
If años < 40:
    if ---- Si, tienes mas de 40 años
    elif ---- Si, tienes menos de 10 años
    else --- No, tienes menos de 40 años o mas de 10 años -> se cumple
'''
# 1- Definicion

# Al ser 5 * 2 = 10, pero nosotros hemos puesto == 11 -> NO SE CUMPLE LA CONDICION
my_condicion = 5 * 2

if my_condicion == 11: 
    print("Se ejecuta la condicion del segundo if")

# Al ser 5 * 2 = 10 y nosotros hemos puesto mayor o igual que 10 -> SE CUMPLE LA CONDICION
my_condicion = 5 * 2

if my_condicion >= 10: 
    print("Se ejecuta la condicion del tercer if")

# Ejecutar una condicion con varias salidas
my_condicion = 5 * 2

if my_condicion > 10:
    print("Es mayor que 10") # No entra por esta variable al ser 10, no mayor
else:
    print("Es menor o igual que 10") # Al ser 10 entra por esta variable <=

# Ejecutar varias opciones de condicion
my_condicion = 5 * 3

if my_condicion > 10 and my_condicion < 20:
    print("Es mayor que 10 y menor que 20") # Entra por esta variable al ser no ser mayor que 10 y menor que 20
else:
    print("Es menor o igual que 10 o mayor o igual que 20") # No entra por esta variable al ser no ser menor que 10 y mayor que 20

# Ejecutar varias condificones (if, elif, else)
my_condicion = 5 * 2

if my_condicion < 10 and my_condicion < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condicion != 15:
    print("Es diferente a 15") # Entra por esta variable es diferente a 15
else:
    print("Es menor o igual que 10 o mayor o igual que 20 y es diferente a 15") 

# Condiciones con cadenas
my_string = "Mi cadena de texto"

if my_string == "Mi cadena de testo":
    print("Mi cadena de texto coincide")
else:
    print("Mi cadena de texto no coincide")

# Condiciones contrarias 
my_string = "Mi cadena de texto"

if not my_string == "Mi cadena de testo": # -> Si que se esta cumpliendo, porque my_string no es igual a "Mi cadena de testo"
    print("Mi cadena de texto coincide")
else:
    print("Mi cadena de texto no coincide")



