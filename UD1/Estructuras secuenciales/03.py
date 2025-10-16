### 3. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

# Nos quedamos con el valor del usuario 
minutosUsuario = int(input("Escribe los minutos que quieres pasar: \n"))

horas = minutosUsuario // 60 # Nos quedamos con el valor entero para las horas
minutos = minutosUsuario % 60 # Nos quedamos con el resto de la operacion para los minutos

# Si las horas es más de uno mostramos horas en vez de hora
if horas > 1:
    print(horas , "horas y", minutos, "minutos")
else:
    print(horas , "hora y", minutos, "minutos")


