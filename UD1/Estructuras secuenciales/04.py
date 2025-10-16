### 4. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

# Introduce un numero de dos cifras
num = str(input("Introduce un numero de 2 cifras: \n"))

# Mientras la longitud sea diferente de 2, vamos a pedur al usuario que me introduzca dos cifras
while len(num) != 2:
    print("Debes introducir un numero de 2 cifras")
    num = str(input("Introduce un numero de 2 cifras: \n"))

# Lo mostramos si es de 2 cifras, con ::-1 que comience por el final
print("El numero invertido es: " , num[::-1])