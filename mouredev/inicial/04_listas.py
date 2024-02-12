### Listas ###

# 1- Definicion de una lista
my_list = list()
my_other_lsit = [7, 7, 7, 7, 7]
'''
Orden de listas
my_list = [1, 5, "hola", 8]
el orden seria -> 0, 1, 2, 3...
1 = 0  / 5 = 1  / "hola" = 2 / 8 = 3
'''
my_list = list()
print(len(my_list)) # -> da 0 porque no tiene ningun elemento en la lista

my_list = [23, 1.75, "Noel", 4, 72, 4]
print(len(my_list))  # -> da 6 porque tiene 5 elemento en la lista

print(type(my_list)) #-> Tipo lista, no el de los elementos que tiene dentro

# 2- Seleccionar elementos dentro de la lista
print(my_list[1]) #-> el elemento 1 de la lista es el 23 (en los positivos el orden empieza por 0)
print(my_list[-1]) #-> el elemento -1 seria el 72 (en los negativos el orden empieza por -1)
#print(my_list[-8]) #-> Error -> no tenemos suficientes elementos en la lista.

print(my_list.count(4))# -> devuelve el nº de repeticiones de un elemento dentro de la lista

# 3- Variables x listas

años, altura, nombre, numero1, numero2, numero3 = my_list
print(años)

altura, nombre, años = my_list[1], my_list[2], my_list[0]
print(años)

# 4- Sumar listas
print(my_list + my_other_lsit) # -> Concatena listas en el orden que se introduce

# 5- Modificar una lista y funciones

my_list.append("Ripollet") #-> añade el elemento al final. SOLO PUEDE 1 ELEMENTO
print(my_list)

my_list.insert(1, "Rojo") #-> añade el elemento en la posicion que tu eligas. SOLO PUEDE 1 ELMENEOT
print(my_list)

my_list[1] = "Amarillo" #-> substituye el elemento de la posicion escogida por el nuevo. Rojo x Amarillo
print(my_list)

my_list.remove(1.75) #-> elimina el primer elemento que coincide con el introducido
print(my_list)

del my_list[2] #-> eliminas el elemento seleccionado, sin guardarlo
print(my_list)

my_list.pop() #-> elimina, pero guarda, el ultimo elemento por defecto
print(my_list.pop()) #-> imprime el ultimo elemento por defecto
print(my_list.pop(2)) #-> imprime el elemento indicado empezando por el final
print(my_list)

my_new_list = my_list.copy() #-> copia la lista y crea otra
print(my_list)
print(my_new_list)

my_new_list.reverse() # Ordena los valores del reves
print(my_list)
print(my_new_list)

del my_list[1]
my_list.sort() # Ordena los valores de menor a mayor o por orden alfabetico, pero no puede combinarse 
print(my_list)
print(my_new_list)

my_list.clear() # -> vacia la lista
print(my_list)
print(my_new_list)

# 6- Sublistas
print(my_new_list[1:3])
