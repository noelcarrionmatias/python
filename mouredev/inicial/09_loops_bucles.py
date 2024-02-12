# loop-bucles

'''
Sirve para pasar por el mismo codigo varias veces
'''

# 1- Tipos de bucles-loops

# 1.1 BUCLE While
'''
Hay que pasarle una condicion. Seria un "mientras" esto sea X haz esto. Cuando ya no sea X para
Seria un IF infinito. Tambien se le puede poner un else (opcional)
'''
my_condition = 0 # -> Al no cumplirse no se ejecuta. Si la condicion cumple y no cambia es un infinito
while my_condition < 10:
    print(my_condition)
    my_condition += 2 # -> Hace que cambie el valor de my_condition, sino seria infinito
else: # Los else son optativos
    print("Mi condicion ya es igual o mayor que 10")

    # break en While
    my_condition = 0 
    while my_condition < 20: 
        my_condition += 1
        if my_condition == 9:
            print(my_condition)
            break # El break sirve para parar el while cuando cumpla una condicion interna, aunque no haya terminado el while
        print(my_condition)

# 1.2 BUCLE For
'''
Se ejecuta tantas veces como nº de elementos tengamos.
Si tenemos 40 elementos, se ejecutará 40 veces.
Puede interactuar con listas, sets, tuplas o diccionarios
Acepta if/ELSE (opcional)
Para parar el bucle -> break
Continue -> para seguir con el bucle aunque haya cumplido una condicion interna (no aconsejable)
'''
my_list = [25, 46, 50, 1, 17, 33]
for element in my_list:
    print(element)

my_list = [25, 46, 50, 1, 17, 33]
for wrgjqeibg in my_list: #element puede ser otra palabra
    print(wrgjqeibg)

my_tuple = (29, 1.75, "noel", "carrion")
for element in my_tuple:
    print(element)

my_set = {"Noel", "Carrion", 29, 1.75}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Noel", "Apellido":"Carrion", "Edad":29, 1:"Python", 2:2} #en diccionario imprime las claves. Le puedes pedir los valores tambien
for element in my_dict:
    print(element)

for element in my_dict:
    print(element)
else: # tambien acepta else, pero opcional
    print("El bucle for para diccionario ha finalizado")

    #break en for
    for element in my_dict:
        print(element)
        if element == "Apellido":
            break # Rompe el bucle en el elemento "Apellido"
        print("Se ejecuta")
    else:
        print("El bucle for para diccionario ha terminado")
    
    #continue en for
    for element in my_dict:
        print(element)
        if element == "Apellido":
            continue # No rompe el bucle en el elemento "Apellido"
        print("Se ejecuta")
    else:
        print("El bucle for para diccionario ha terminado")
