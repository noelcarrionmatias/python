### classes

# 1- Definir classes

class Person: #El nombre de las classes van primera en mayuscula y el resto en minuscula. ej: MyClassOne
    pass # -> Si no le añadimos nada a classes dará error.

''' 
ESTO DA ERROR

class Person: 
'''    

# 2- definir propiedades de clase fuera
class Person:
    def __init__(self, name, surname, alias = "sin alias"): #alias lleva un valor predefinido por si no se le agrega uno despues
        self.fullname = f"{name} {surname} {alias}" 
        #pass #Si se introducen valores a los parametros hay que quitar pass

my_person = Person("Noel", "Carrion") # aqui se definen los valores de las propiedades. 
print(my_person.fullname)

# 3- definir propiedades de clase dentro
class Person:
    def __init__(self): #init define el constructor para recibir parametros de la clase. self es obligatorio
        self.name = "noel" #aqui se definen los valores de las propiedades
        self.surname = "carrion" #aqui se definen los valores de las propiedades
        self.alias = "ncm" #aqui se definen los valores de las propiedades
        #pass #Si se introducen valores a los parametros hay que quitar passç
    
    def walk(self): #se pueden definir mas parametros
        print(f"{self.name} Esta caminando")

my_person = Person() #al tener valores definidos dentro de clase no hace falta nombrarlos aqui
print(my_person.name) #hay que llamar a los parametros que quieres mostrar
my_person.alias = "cocodrilo" #asi se puede cambiar un valor por otro
print(my_person.alias)