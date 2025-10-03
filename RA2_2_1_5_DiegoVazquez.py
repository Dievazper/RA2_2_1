# Autor: Diego Vazquez
# Data: 3-10-25

# Descripció del programa o enunciat de l'exercici:
    # Escriu un programa que demani la data de naixement i digui si és major o menor d'edat.
# Especificacions d'entrada
    # La any de naixement

    # El any actual

# Especificacions de sortida
    # Missatge que indiqui si és major o menor d'edat

any_naixament=int(input("Introdueix el teu any de naixament:  "))

any_actual=int(input("Introdueix l'any actual:  "))

edad_actual=any_actual- any_naixament

if edad_actual>=18: 
    print("Es major de edad")
else:
    print("Es menor de edad")