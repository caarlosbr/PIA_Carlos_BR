### 6. Escribir un programa para calcular la nota final de un examen, considerando que:

## Cada respuesta correcta suma 5 puntos.
## Cada respuesta incorrecta suma -1 puntos.
## Cada respuesta en blanco suma 0 puntos. 
## Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

preguntasCorrectas = int(input("Cuantas preguntas correctas tuviste:\n"))
preguntasSin = int(input("Cuantas preguntas sin responder tuviste:\n"))
preguntasIncorrectas = int(input("Cuantas preguntas incorrcetas tuviste:\n"))

total = 0

puntosCorrectas = preguntasCorrectas * 5
puntosIncorrectas = preguntasIncorrectas * (-2)
# print(puntosCorrectas, puntosIncorrectas)

total = puntosCorrectas + puntosIncorrectas

print("Tu nota final es:", total / 5)