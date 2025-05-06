
umbral_seguridad = 70.0

def obtener_temperatura():
    return float(input("Ingrese la temperatura actual de la banda transportadora: "))

temperatura = obtener_temperatura()


if temperatura > umbral_seguridad:
    alerta = "La temperatura excede el límite de seguridad."
else:
    alerta = "Temperatura en rango seguro."


print(alerta)