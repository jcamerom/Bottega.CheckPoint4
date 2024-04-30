# CHECKPOINT 4

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
ej_integer = 42
ej_float = 4.82

from decimal import Decimal
ej_decimal = Decimal(3.141592)

ej_lista = ['Mayo', 'Abril', 'Junio']

ej_tupla = (4, 0, 'Febrero', 6.52)

ej_diccionario = {
    'tomates': 3.42,
    'higos': 5.91,
    'sandias': 2.65 
}

# Exercise 2: Round your float up.
import math
print(math.ceil(ej_float))

# Exercise 3: Get the square root of your float.
print(math.sqrt(ej_float))

# Exercise 4: Select the first element from your dictionary.
first_element = ej_diccionario['tomates']
print(first_element)

# Exercise 5: Select the second element from your tuple.
second_element = ej_tupla[1]
print(second_element)

# Exercise 6: Add an element to the end of your list.
ej_lista.append('Octubre')
print(ej_lista)

# Exercise 7: Replace the first element in your list.
ej_lista[0] = 'Primer'
print(ej_lista)

# Exercise 8: Sort your list alphabetically.
ej_lista.sort()
print(ej_lista)

# Exercise 9: Use reassignment to add an element to your tuple.
ej_tupla += ('Fin',)
print(ej_tupla)