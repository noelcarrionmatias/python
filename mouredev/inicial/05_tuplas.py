### Tuplas ###
'''
La principal diferencia entre tupla y lista es
que la inmutabilidad de los datos, es decir,
una vez definida no se puede modificar o añadir nuevos elementos

ejemplo:

my_tuple[1] = 1.88 -> 'tuple' object does not support item assignment

Lo que si puedes es sumar varias tuplas para crear una nueva
Tambien eliminarla del todo, no variarla -> del my_tuple -> desaparece la tupla
'''
# 1- definición de tuplas 
my_tuple = tuple()
my_other_tuple = () #-> listas es con []

my_other_tuple = (29, 1.75)
my_tuple = (29, 1.75, "noel", "carrion")
print(my_tuple)
print(type(my_tuple))

# 2- seleccionar elementos de la tupla
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[3])
print(my_tuple[-2])
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

# 3- operaciones
print(my_tuple.count(29)) # -> cuenta cuantos 29 hay
print(my_tuple.index("carrion"))

# 4- cambio de tupla a lista -> ahora si que puede modificarse
my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple[1] = 1.88 #modificamos campo 1
my_tuple.insert(4, "azul") #añadimos campo 4
print(my_tuple)
my_tuple = tuple(my_tuple)
print(type(my_tuple))
