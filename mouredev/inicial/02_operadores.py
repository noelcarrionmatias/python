#### 1- Operadores artimeticos ####

print(3 + 4) #Suma
print(3 - 4) #Resta
print(3 * 4) #Multiplica
print(3 / 4) #Divide
print(10 % 3) #Resto (lo que sobra de la división)
print(10 // 3) #Floor division. Hace la división a un numero aproximado (siempre da numero entero)
print(2 ** 3) #Numero elevado a 

#Tambien funciona con texto
print("Hola" + "Python") #Concatena cadenas de texto
# print("Hola" -  "Python") #Error -> Solo no es posible restar cadenas de texto

#print("Hola" + 5) #Error -> No combina diferentes tipos de datos
print("Hola" + str(5)) #Ahora si, al ser 5 un str como "Hola"

print("Hola" * 5) #Te multiplica el str * 5 -> aparecen 5 veces

#### 2- Operadores comparativos ####

#Devuelven True / False
print(3 < 4) #Menor que
print(3 > 4) #Mayor que
print(3 <= 4) #Menor o igual que
print(3 >= 4) #Mayor o igual que
print(3 == 4) #Igual que
print(3 != 4) #Diferente que

#En comparativos de textos, tiene en cuenta la ordenación alfabética. Tiene en cuenta las mayusculas
print("Hola" < "Python") #Menor que
print("Hola" > "Python") #Mayor que
print("Hola" <= "Python") #Menor o igual que
print(len("Hola") <= len("Python")) #Menor o igual que -> Tiene en cuenta el numero de caracteres
print("Hola" >= "Python") #Mayor o igual que
print("Hola" == "Python") #Igual que
print("Hola" != "Python") #Diferente que

#### 3- Operadores lógicos ####

print(3 > 4 and "Hola" > "Python") #y
print(3 > 4 or "Hola" > "Python") #o
print(3 < 4 and "Hola" < "Python") #y
print(3 < 4 or "Hola" < "Python") #o
#print(3 > 4 not "Hola" > "Python") #no -> Error. El not va antes
print(not(3 > 4)) #Devuelve True porque 3 no es mayor que 4 -> no+no es si