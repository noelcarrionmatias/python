### Diccionarios
'''
Se define igual que el set -> {}
La estructura del dict es clave:valor
La clave debe ser unica -> Si se repite te coge el ultimo valor
'''
# 1- Definicion y estructura

my_dict = dict()
print(type(my_dict))
my_other_dict = {}
print(type(my_other_dict))

my_other_dict = {"Nombre":"Noel", "Apellido":"Carrion", "Edad":29} # Clave:valor
print(my_other_dict)

my_other_dict = {"Nombre":"Noel", "Apellido":"Carrion", "Edad":29, 1:"Python", 2:2} # La clave:valor pueden ser numeros
print(my_other_dict)

my_dict = {
    "Nombre":"Noel",
    "Apellido":"Carrion",
    "Edad":29, 
    1:"Python", 
    2:2,
    "Lenguajes": {"Java", "HTML", "CSS"},
    1:"Hola"
    } # Se pueden agregar diferentes valores a una clave. Solo puede haber CLAVES unidas, sino coge el ultimo clave:valor
print(my_dict)

# 2- Acceder a valores
print(len(my_dict)) # -> cuenta el numero de claves:valores

print(my_dict["Nombre"]) # -> Al acceder a la clave te imprime el valor

my_dict["Nombre"] = "Mery" #Substituye el valor
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle Noel" # Agregar nuevos valores
print(my_dict)

# 3- Operaciones
del my_dict["Calle"] # Borra un clave:elemento del diccionario
print(my_dict)

print("Mery" in my_dict) # Detecta si "Mery" esta dentro, pero solo por el campo CLAVE
print("Nombre" in my_dict) # Ahora si, porque "Nombre" es una clave

print(my_dict.items()) # Devuelve un listado de cada Clave:Valor
print(my_dict.keys()) # Devuelve un listado de las claves
print(my_dict.values()) # Devuelve un listado de los valores

print(my_dict.fromkeys(("Nombre", 1))) # -> Devuelve un nuevo diccionario con claves, pero sin valores
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # -> Asi tambien se puede crear un diccionario nuevo, incluso nuevas claves
print(my_new_dict)
my_new_dict = my_dict.fromkeys(("Nombre", 1))
print(my_new_dict)
my_new_dict = my_dict.fromkeys(my_dict, "Pais") # Tambien heredar las claves de otro diccionario + nuevas claves
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Noel", "Carrion")) # Se duplican los valores a todas las claves
print(my_new_dict)
'''
{'Nombre': ('Noel', 'Carrion'), 'Apellido': ('Noel', 'Carrion'), 'Edad': ('Noel', 'Carrion'),
 1: ('Noel', 'Carrion'), 2: ('Noel', 'Carrion'), 'Lenguajes': ('Noel', 'Carrion')}
'''
# 4- Cambiar de lista a dict

my_list = ["Nombre", 1, "Piso"] # Los elementos de la lista son la clave del diccionario
print(my_list)
print(type(my_list))
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
print(type(my_new_dict))