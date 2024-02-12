### modules
'''
Usar ficheros o codigos fuera de nuestro fichero.
Es como usar nuestro otro codigo como una libreria externa
No conectará correctamente con los codigos cuyo nombre empiece por numero (1, 3, 8...)
'''

# 1- Importar todo de un codigo
'''
import
"10_functions".my_function()
'''
# 2- Importar una parte del codigo
'''
from '10_functions' import sum_two_values, sum_two_values_with_return #Puede acceder a varias a la vez 
my_function()
'''
# 3- Otras librerias

import random
print(random.random())

import math
print(math.pi)