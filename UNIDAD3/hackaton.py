
pregunta = input("desea agregar mandado si/no:").strip().lower()

if pregunta == "si":
    num_articulos = int(input("¿cuantos articulos va a querer mijo?"))
    lista_compras = []
    for i in range(num_articulos):
        compra = input(f"ingresa el nombre del producto {i + 1}:").strip()
        lista_compras.append(compra)
        print("lista de articulos")
        for compra in lista_compras:
            print(f"- {compra}")
    
    print("Ahinomasquedoplebes")
else:
    print("Nimodo de todos modos no le vendemos a prietos")
