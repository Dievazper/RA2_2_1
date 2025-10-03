# Autor: Diego Vazquez
# Data: 3-10-25

# Descripció del programa o enunciat de l'exercici:
    # Escriu un programa que demani tres números i digui quin és el més gran.
# Especificacions d'entrada
    # Tres números enters
# Especificacions de sortida
    # Et diu quin es mes gran

num1= int(input("Introdueix un numero: "))
num2= int(input("Introdueix un numero: "))
num3= int(input("Introdueix un numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número més gran és:{num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número més gran és:{num2}")
else:
    print(f"El número més gran és:¨{num3}")