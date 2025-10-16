### 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un programa que determine la hora de llegada a la ciudad B.
horasA = int(input("Introduce a que hora sales de CiudadA:\n"))
minutosA = int(input("Introduce a que minuto sales de CiudadA:\n"))
segundosA = int(input("Introduce a que segundos sales de CiudadA:\n"))

print("Sales a las:", horasA, "h", minutosA, "mins", segundosA, "sgs")
segundosTotalesA = (horasA * 60 * 60) + (minutosA * 60) + segundosA

segundosB = int(input("CUantos segundos se tardan en llegar a ciudad B: \n"))

segundosTotalesSumar = segundosTotalesA + segundosB
print(segundosTotalesSumar)

horaLlegada = segundosTotalesSumar // 3600
minutosLlegada = int((segundosTotalesSumar % 3600) / 60)
segundosLlegada = segundosTotalesSumar % 60

print("Llegas a las:", horaLlegada, "h", minutosLlegada, "mins", segundosLlegada, "sgs")
