Algoritmo Medicion_Temperatura
    
    Definir temperatura Como Real
    Definir umbral_seguridad Como Real
    Definir alerta Como Cadena
	
    
    umbral_seguridad = 70.0  
	
    
    Escribir "Ingrese la temperatura actual de la banda transportadora:"
    Leer temperatura
	
    
    Si temperatura > umbral_seguridad Entonces
        alerta = "¡Alerta! La temperatura excede el límite de seguridad."
    Sino
        alerta = "Temperatura en rango seguro."
    FinSi
	
    // ya nomas se cambiaria en vez de que pidala temperatura que lo lea del sensor 
    Escribir alerta
FinAlgoritmo

