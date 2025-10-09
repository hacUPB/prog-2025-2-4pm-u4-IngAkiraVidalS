# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")

#calcular el promedio de la velocidad
suma = 0
for v in velocidad:
    suma += v

promedio = suma / len(velocidad)
print(f"velocidad promedio = {promedio}")

#imprimir las velocidades por encima del promedio 
print("velocidades por encima del promedio:") 
for v in velocidad:
    if v > promedio:
        print(v)
        
