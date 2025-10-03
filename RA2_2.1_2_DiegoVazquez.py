# Autor: Diego Vazquez 
# Data: 3-10-25

# Descripció del programa o enunciat de l'exercici:

    #Programa que diu si un número és parell o imparell

# Especificacions d'entrada

    #Introduir un número

# Especificacions de sortida

    #Missatge dient si és parell o imparell

numero=int(input("Introdueix un numero: "))
if numero %2==0:
    print(f"El numero {numero} es parell")
else:
    print(f"El numero {numero} es senar")
    