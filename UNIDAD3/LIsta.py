# Lista vacía para almacenar los productos
lista_compras = []

print("🛒 Lista de Compras 🛒")

# Agregar productos
producto1 = ("caguama")
lista_compras.append(producto1)

producto2 = ("Doritos")
lista_compras.append(producto2)

producto3 = ("papas ")
lista_compras.append(producto3)

# Mostrar la lista completa
print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")

producto = int(input("que productto desea comprar?"))



