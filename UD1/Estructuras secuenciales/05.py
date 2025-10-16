### 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un programa que determine la hora de llegada a la ciudad B.

# Guardamos las horas, minutos, y segundos desde que salimos de la ciudad A
horasA = int(input("Introduce a que hora sales de CiudadA:\n"))
minutosA = int(input("Introduce a que minuto sales de CiudadA:\n"))
segundosA = int(input("Introduce a que segundos sales de CiudadA:\n"))

# Mostramos a la hora,minutos y segundos que salimos 
print("Sales a las:", horasA, "h", minutosA, "mins", segundosA, "sgs")

# guardamos en segundos la hora de ese momento 
segundosTotalesA = (horasA * 60 * 60) + (minutosA * 60) + segundosA

# le preguntamos al usuario cuantos segundos se tardan en llegar a la ciudad B
segundosB = int(input("CUantos segundos se tardan en llegar a ciudad B: \n"))

# guardamos la hora de llegada en segundos
segundosTotalesSumar = segundosTotalesA + segundosB
print(segundosTotalesSumar)

# guardamos la hora de llegada en entero 
horaLlegada = segundosTotalesSumar // 3600
# guardamos los minutos de llegada 
minutosLlegada = int((segundosTotalesSumar % 3600) / 60)
# guardamos los segundos de llegada 
segundosLlegada = segundosTotalesSumar % 60

# Mostramos a que hora llegaria
print("Llegas a las:", horaLlegada, "h", minutosLlegada, "mins", segundosLlegada, "sgs")
