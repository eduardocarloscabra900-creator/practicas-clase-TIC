#proyecto paecial 2
tiendita = [
    {"id": 1, "nombre": "Sabritas", "categoria": "Botanas", "precio": 15, "existencia": 20},
    {"id": 2, "nombre": "Coca-Cola 600ml", "categoria": "Bebidas", "precio": 20, "existencia": 30},
    {"id": 3, "nombre": "Galletas Oreo", "categoria": "Dulces", "precio": 18, "existencia": 12},
    {"id": 4, "nombre": "Lápiz", "categoria": "Papelería", "precio": 5, "existencia": 50},
]


def mostrar_producto(prod):
    print("codigo: prod['codigo']  prod['nombre']  prod['categoria']  prod['precio']  Existencia: prod['existencia']")


def agregar_producto():
    print("--- AGREGAR PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría (Botanas, Bebidas, Dulces, Papelería, etc.): ")
    precio = float(input("Precio: $"))
    existencia = int(input("¿Cuántos hay en existencia?: "))
    nuevo_codigo= len(tiendita) + 1
    
    while any(p["codigo"] == nuevo_codigo for p in tiendita):
        nuevo_codigo += 1
    producto = {"codigo": nuevo_codigo, "nombre": nombre, "categoria": categoria, "precio": precio, "existencia": existencia}
    tiendita.append(producto) 
    print("¡Producto agregado!")


def consultar_productos():
    print("--- TODOS LOS PRODUCTOS ---")
    if not tiendita:
        print("No hay productos registrados.")
    else:
        for prod in tiendita: 
            mostrar_producto(prod)


def buscar_producto():
    print("--- BUSCAR PRODUCTO ---")
    busqueda = input("Escribe el ID o el nombre: ")
    for prod in tiendita:
        if str(prod["codigo"]) == busqueda or prod["nombre"].lower() == busqueda.lower():
            mostrar_producto(prod)
            return
    print("No se encontró ese producto.")


def modificar_producto():
    print("--- MODIFICAR PRODUCTO ---")
    id_buscar = int(input("codigo del producto a modificar: "))
    for prod in tiendita:
        if prod["codigo"] == id_buscar:
            print("Deja en blanco si no quieres cambiarlo")
            nuevo_nombre = input(f"Nombre actual ({prod['nombre']}): ")
            nueva_categoria = input(f"Categoría actual ({prod['categoria']}): ")
            nuevo_precio = input(f"Precio actual (${prod['precio']}): ")
            nueva_existencia = input(f"Existencia actual ({prod['existencia']}): ")
           
            if nuevo_nombre == "":
                prod["nombre"] == nuevo_nombre
            if nueva_categoria == "":
                prod["categoria"] == nueva_categoria
            if nuevo_precio == "":
                prod["precio"] == float(nuevo_precio)
            if nueva_existencia == "":
                prod["existencia"] == int(nueva_existencia)
            print("¡Producto modificado!")
            return
    print("No existe ese codigo.")


def eliminar_producto():
    print("--- ELIMINAR PRODUCTO ---")
    id_buscar = int(input("codigo del producto a eliminar: "))
    for prod in tiendita:
        if prod["codigo"] == id_buscar:
            tiendita.remove(prod) 
            print("¡Producto eliminado!")
            return
    print("No existe ese codigo.")


def contar_productos():
    print(f"Total de productos diferentes: {len(tiendita)}")
    total_piezas = 0
    for prod in tiendita:
        total_piezas += prod["existencia"]
    print(f"Total de piezas en la tiendita: {total_piezas}")


def ordenar_productos():
    print("--- PRODUCTOS ORDENADOS POR PRECIO (de menor a mayor) ---")
    ordenados = sorted(tiendita, key=lambda x: x["precio"]) 
    for prod in ordenados:
        mostrar_producto(prod)


def filtrar_productos():
    print("--- FILTRAR POR CATEGORÍA ---")
    criterio = input("Escribe la categoría (Botanas, Bebidas, Dulces, Papelería): ")
    encontrados = 0
    for prod in tiendita:
        if prod["categoria"].lower() == criterio.lower():
            mostrar_producto(prod)
            encontrados += 1
    if encontrados == 0:
        print("No se encontró nada con esa categoría.")


def reporte_general():
    print("--- REPORTE GENERAL ---")
    print(f"Total de productos diferentes: {len(tiendita)}")
    valor_total = 0
    for prod in tiendita:
        valor_total += prod["precio"] * prod["existencia"]
    print(f"Valor total de la tiendita: ${valor_total}")
    print("Lista completa:")
    for prod in tiendita:
        mostrar_producto(prod)


def vender_producto():
    print("--- VENDER PRODUCTO ---")
    id_buscar = int(input("codigo del producto a vender: "))
    for prod in tiendita:
        if prod["codigo"] == id_buscar:
            if prod["existencia"] > 0:
                prod["existencia"] -= 1
                print(f"¡Vendido 1 {prod['nombre']}! Te quedan {prod['existencia']}.")
            else:
                print("Ya no hay existencia de ese producto.")
            return
    print("No existe ese codigo.")


def menu():
    while True:
        print("===== SISTEMA DE TIENDITA =====")
        print("1. Agregar producto")
        print("2. Consultar todos los productos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Contar productos")
        print("7. Ordenar productos por precio")
        print("8. Filtrar por categoría")
        print("9. Reporte general")
        print("10. Vender producto")
        print("11. Salir")  # REQUISITO: Salir del sistema
        opcion = input("Elige una opción (1-11): ")


        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            contar_productos()
        elif opcion == "7":
            ordenar_productos()
        elif opcion == "8":
            filtrar_productos()
        elif opcion == "9":
            reporte_general()
        elif opcion == "10":
            vender_producto()
        elif opcion == "11":
            print("¡Gracias por comprar en la tiendita! Adiós.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Aquí empieza el programa
menu()