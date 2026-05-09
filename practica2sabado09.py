def compras(n):
    total = 0

    for i in range(n):
        print(f"\nProducto {i + 1}")
        valor = float(input("Ingrese el valor del producto: "))

        etiqueta = 0
        while etiqueta < 1 or etiqueta > 1000:
            etiqueta = int(input("Ingrese el numero de la etiqueta (1 - 1000): "))
            if etiqueta < 1 or etiqueta > 1000:
                print("Numero fuera de rango. Ingreselo nuevamente.")

        if etiqueta == 666:
            descuento = valor * (20 / 100)
            valor = valor - descuento
            print(f"Descuento aplicado: {descuento}")

        total += valor

    print("\n********Total a Pagar**********")
    print(f"El total final a pagar es: {total} Bs")

print("********Tienda El Diablo**********")
n = int(input("Introduzca la cantidad de productos: "))
compras(n)