### Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

persona1 = int(input("Introduce la edad de la primera persona \n"))
persona2 = int(input("Introduce la edad de la segunda persona \n"))

if persona1 > persona2:
    print("La más joven es la persona 2 con", persona2, "años")
elif persona2 > persona1:
    print("La más joven es la persona 1 con", persona1, "años")
else:
    print("Las dos personas tienen la misma edad")

