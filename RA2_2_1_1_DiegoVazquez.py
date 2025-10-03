# Autor: Diego Vazquez
# Data: 3-10-25

# Descripció del programa o enunciat de l'exercici:

    # Programa que diu si un número és més gran, més petit o igual que 0

# Especificacions d'entrada:

    #Introduir un número

# Especificacions de sortida

    #Missatge dient si és més gran, més petit o igual que 0
 
num1=int( input("Introdueix un numero: "))
if num1 > 0:
    print("Es mes gran que 0")
if num1 < 0 :
    print ("Es mes petit que 0")
if num1 == 0:
    print ("Es igual que 0")