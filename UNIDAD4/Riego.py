humedad = None

while True:
    print("---- MENÚ ----")
    print("1. Ingresar humedad")
    print("2. Mostrar humedad actual")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))
    
    if opcion == 1:
        humedad = float(input("Ingrese el valor de la humedad (%): "))
        print("Humedad registrada con éxito.")
    elif opcion == 2:
        if humedad is not None:
            print(f"Humedad actual: {humedad}%")
            if humedad < 40:
                print("Humedad baja. Activando riego...")
            else:
                print("Humedad suficiente. No se activa riego.")
        else:
            print("No se ha ingresado la humedad aún. Por favor, seleccione la opción 1 primero.")
    elif opcion == 3:
        print("Fin del programa.")
        break
    else:
        print("Opción no válida.")