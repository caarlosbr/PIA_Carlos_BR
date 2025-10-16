### 2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

# cat1 = 9
# cat2 = 1

# Pedimos al usuario que introduzca el primer coseno
cat1 = int(input("Introduce el número del primer coseno: \n"))

# Pedimos al usuario que introduzca el segundo coseno
cat2 = int(input("Introduce el número del segundo coseno: \n"))

# Hacemos la fórmula de la hipotenusa, es c=sqrt(a^2+b^2)
hip = ((cat1 ** 2) + (cat2 ** 2)) ** 0.5

# Mostramos el resultado
print(hip)