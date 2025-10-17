### Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.
from prompt_toolkit.renderer import print_formatted_text

cat1 = int(input("Introduce el primer cateto del triangulo \n"))
cat2 = int(input("Introduce el segundo cateto del triangulo \n"))
hip = int(input("Introduce la hipotenusa del triangulo \n"))

hipPitagoras = ((cat1 ** 2) + (cat2 ** 2)) ** 0.5


print(hipPitagoras)
