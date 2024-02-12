# Excepciones

'''
Sirve para manejar las excepciones de los errores
y no falle todo. 
Posibilita que el codigo siga ejecutandose a pesar de haber un error
'''
numberOne, numberTwo = 5, 1
numberTwo = "1"
#print(numberOne + numberTwo) # ->  Da error (excepcion)

# 1- Definicion

try: #obligatorio
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: #obligatorio
    #Se ejecuta cuando try salta error. Si hay una excepcion
    print("Se ha producido un error") 
else: #optativo
    #Esta se ejecuta si en try no hay error. Si no hay una excepcion
    print("La ejecución continua correctamente") 
finally: #optativo
    #Se ejecuta siempre
    print("La ejecución continua") 

# 2- Captura de errores/excepciones por typo

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError: #Se ejecuta solo si se produce ValueError
    print("Se ha producido un ValueError") 
except TypeError: #Se ejecuta solo si se produce TyperError
    print("Se ha producido un TypeError")
except Exception: #Es un tipo de error generico
    print("Se ha producido una Exception")

# 3- Captura de la información de la excepcion

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error1: #No se ejecuta porque no es un ValueError
    print(error1) 
except Exception as excepcion: #Es un tipo de error generico. Se ejecuta si las excepciones de antes no aciertan
    print(excepcion) #muestra el tipo de error que tienes