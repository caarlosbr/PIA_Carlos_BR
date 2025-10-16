### 6. Escribir un programa para calcular la nota final de un examen, considerando que:

## Cada respuesta correcta suma 5 puntos.
## Cada respuesta incorrecta suma -1 puntos.
## Cada respuesta en blanco suma 0 puntos. 
## Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

# Creamos un while para que en caso de que el usuario introduzca un total de preguntas diferente a 10
# de error y tenga que meter obligatoriamente 10 preguntas, ya que mi examen tiene 10 preguntas
while True:

    # Le preguntarmos al usuarios cuantas preguntas bien, sin responder, e incorrectas
    preguntasCorrectas = int(input("Cuantas preguntas correctas tuviste:\n"))
    preguntasSin = int(input("Cuantas preguntas sin responder tuviste:\n"))
    preguntasIncorrectas = int(input("Cuantas preguntas incorrcetas tuviste:\n"))

    # guardamos el numeroPreguntas el numero de las preguntas, para comprobar si es 10
    numeroPreguntas = preguntasCorrectas + preguntasIncorrectas + preguntasSin

    # Si es 10 sigue el ciclo del while
    if numeroPreguntas == 10:

        # Multiplicamos por 5 que es lo que vale cada pregunta bien
        puntosCorrectas = preguntasCorrectas * 5

        # Multiplicamos por -2 por cada pregunta mal
        puntosIncorrectas = preguntasIncorrectas * (-2)
        # print(puntosCorrectas, puntosIncorrectas)

        # Guardamos en total todos los puntos totales
        total = puntosCorrectas + puntosIncorrectas

        # Imprimos la nota final a un valor de 0 a 10
        print("Tu nota final es:", total / 5)
        break
    # Si el valor de numero preguntas es diferente a 10 repetimos el bucle y mostramos el mensaje
    else: 
        print("Debes de introducir 10 preguntas en total, ya que el examen tiene 10 preguntas")


