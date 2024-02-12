### Strings - cadena de texto###

my_string = "Mi string"
my_other_string = 'Mi otro string'

'''
\n hace un salto de linea
\t hace una tabulación
'''
my_new_line_string = "\t Este es un String \n con salto de linea"
print(my_new_line_string)

# 1- Formateo
'''
%s formateo de texto
%d formateo de enteros
%f formateo de numeros decimales
'''
name, apellido, edad = "Noel", "Carrion", 29
print("Mi nombre es {} {} y mi edad es {}".format(name, apellido, edad)) # No hace falta poner %s o %d
print("Mi nombre es %s %s y mi edad es %d" %(name, apellido, edad)) #Hace falta poner %s o %d u otro
print(f"Mi nombre es {name} {apellido} y mi edad es {edad}") #Necesita la "f" delante del todo

# 2- Desempaquetado de caracteres

language = "Python"
#a, b = language -> Error. Te pide tantas variables como nº caracteres que tiene language ("Python")
a, b , c, d, e, f= language #-> una variable x cada caracter
print(a)
print(b)

# 3- Division

language_slice = language[1:3] # coge los caracteres del 1 al 2 (sin contar el 3)
print(language_slice) #-> yt

language_slice = language[1:] # coge los caracteres del 1 al final
print(language_slice) #-> ython

language_slice = language[-2] # coge el caracter x empezando a contar desde el final
print(language_slice) #-> o

language_slice = language[0:6:2] # Coge del caracter 0 al 6 de 2 en 2
print(language_slice) #-> o

# 4- Reverse

reverse_language = language[::-1] # empieza por el final (el -1)
print(reverse_language) #-> ython

# 5- Funciones (hay mas)

#Saber cuantas funciones puedo hacer
'''
print(language.) con poner el . detras de la variable 
'''
#Calcula la longitud del string. Da el mismo resultado
print(len(language))
print(language.__len__())

print(language.capitalize()) #Primera mayuscula
print(language.upper()) #Todas mayusculas
print(language.count("t")) #Cuenta caracteres
print(language.isnumeric()) #True/False si es numero
print("1".isnumeric()) #True/False si es numero
print(language.lower()) #Todo minuscula
print(language.startswith("Py")) #True/False si language (Python) empieza por "py"
print(language.upper().isupper()) #True porque isupper responde T/F su es mayuscula -> upper lo pone en mayuscula

