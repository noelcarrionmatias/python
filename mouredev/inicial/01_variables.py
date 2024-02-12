#Variables

# 1- las variables pueden tener mayusculas, pero lo estandard es todo minuscula y "_" entre palabras
my_variable = "My String variable"
print(my_variable)

my_int_variable = 456132
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# 2- Concatenacion de variables. Pueden llevar varias variables, datos...
print(my_int_variable, my_variable)
print("Este es el valor de:", my_variable)

# 3- Cambio de tipo de dato
#se cambia de tipo de dato: int a str
my_int_to_str_variable = str(my_int_variable)
#devuelve el valor de la variable
print(my_int_to_str_variable)
#escribe que es un tipo de dato: str aunque sean numeros
print(type(my_int_to_str_variable))

# 4- Algunas funciones precargadas del sistema
print(len(my_variable)) #cuenta los caracteres (incluido espacios)

# 5- Variables en una sola linea. Se crean varias variables y toman el valor según el orden
name, surname, alias, age = "Noel", "Carrion", "NCM", 29
print("Me llamo:",name)
print("Me llamo:",name, surname, "y mi edad es:", age)

# 6- Inputs
name = input("Como te llamas?")
age = input("cuantos años tienes?")
#Se reasignan los valores de las variables. Coge el úlimo valor definido
print(name)
print(age)

# 7- Cambio de tipo
"""
El valor de la variable viene definido por el último valor definido. 
name antes era str "noel" y ahora es int "35"
age antes era int "29" y ahora es str "Jose"
"""
name = 35
age = "Jose"
#Se fuerza el cambio de tipo de dato en cada cambio
address = str = "Mi direccion"
address = 42
address = True
print(type(address)) #definirá el type de address como bool (True/False)
