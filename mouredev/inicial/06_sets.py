# SETS 
'''
- Al definir un SETS vacio python lo detecta como un diccionario. Al llenarlo con datos lo detecta como un SET
- No es una estructura ordenada. No tiene indice
- No acepta repeticiones
'''

# 1- Definicion
my_set = set()
my_other_set = {}

print(type(my_set)) # -> set es un tipo de dato
print(type(my_other_set)) # -> Al ponerle {} detecta que es un diccionario

my_other_set = {"Noel", "Carrion", 29, 1.75}
print(type(my_other_set)) # -> Al llenar el SETS con datos ya lo detecta como SETS y no Diccionario


# 2- Algunas operaciones en SET
my_other_set.add("Ripollet") #Un set no es una estructura ordenada, por eso te da el orden aleatoriamente
print(my_other_set)
my_other_set.add("Ripollet") #Aunque ahora se ha vuelto a introducir "Ripollet" otra vez -> no admite repetidos
print(my_other_set)

print("Ripollet" in my_other_set) #Existe la posibilidad de saber si hay o no un valor dentro
print("Ripoll" in my_other_set) #True si esta, False si no esta

my_other_set.clear() # Vacia el set de datos
print(my_other_set)
del my_other_set # Elimina el set
# print(my_other_set) # name 'my_other_set' is not defined

my_set_one = {1, 2, 3, 4}
my_set_two = {4, 5, 6, 7}
my_set_three = my_set_one.union(my_set_two) # Union junta los set, pero sin las repeticiones
print(my_set_three)
my_set_three = my_set_three.union({8, 9, 10}) # Tambien puede juntar el set con valores definidos al momento
print(my_set_three)
my_set_three = my_set_three.union({11, 12, 13}).union({"Carrion", 15}) # Varios union a la vez
print(my_set_three)

print(my_set_one.difference(my_set_three)) # No devuelve diferencias porque my_set_one tiene los mismos valores que my_set_three
print(my_set_three.difference(my_set_one)) # Devuelve diferencias porque my_set_three tiene diferentes valores que my_set_one


# 3- Acceso a elementos del SET
'''
print(my_other_set[1])  # -> Error porque SET no es una estructura ordenada (no es un listado)
'''

# 4- Cambiar de tipo set a lista/tupla
'''
Cambiar SET a lista es arriesgado, ya que cada vez que ejecutas el programa el orden del set antes
de convertirse en lista cambia
'''
my_set = {"Noel", "Carrion", 29, 1.75}
my_list = list(my_set)
print(my_list)
print(my_list[0])



