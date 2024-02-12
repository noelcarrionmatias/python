### Funciones

# 1- definicion

def my_function (): #todo lo que este tabulado despues de la funcion formará parte de ella
    print("Esto es una funcion")

my_function() # -> Para llamar a la funcion

# 2- introducir parametros 
def sum_two_values (first_number, second_number): #entre () se le agregan los parametros que tendrá en cuenta
    print( first_number + second_number)

sum_two_values(5, 7) #al llamar la funcion es cuando hay que definirle los parametros que se nombran en la funcion
sum_two_values("5", "ajbdfwjufbwi") #Tienen que ser el mismo tipo de dato

# 3- retorno de funcion
def sum_two_values_with_return (first_number, second_number): 
    return first_number + second_number #esta funcion no hace un print, sino un retorno que se le agrega a una variable

my_result = sum_two_values_with_return(10, 5) #-> devuelve el resultado
print(my_result)
my_result = sum_two_values(5, 7) #-> no devuelve nada
print(my_result)

# 4- ordenar parametros de funcion
def print_name (name, surname): #Se define el orden de salida de los parametros
    print(name, surname) 

print_name(surname= "Carrion", name= "Noel") #aunque le pongamos el orden contrario la funcion los ordena

# 4- parametros por defecto
def print_name_with_default (name, surname, alias = "Sin alias"): #alias por defecto tiene el valor "Sin alias"
    print(name, surname, alias) 

print_name_with_default(surname= "Carrion", name= "Noel") #Al no definirse el valor de alias, se muestra el valor por defecto
print_name_with_default(surname= "Carrion", name= "Noel", alias= "NCM") #Al definirse el valor de alias, no se muestra el valor por defecto

# 5- Numero de parametros dinamico + bucle FOR

def print_text(*texts):
    for text in texts:
        print(text.upper())

print_text("Hola", "adios")