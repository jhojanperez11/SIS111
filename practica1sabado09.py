def calcular_bonos(n):
    total_locomocion = 0
    total_alimentacion = 0

    for i in range(n):
        print(f"\nTrabajador {i + 1}")
        ci = int(input("Ingrese el CI del trabajador: "))

        sueldo = 0
        while sueldo < 5000:
            sueldo = int(input("Ingrese el sueldo (minimo de 5000 Bs): "))
            if sueldo < 5000:
                print("El sueldo no puede ser menor a 5000 Bs. Ingreselo nuevamente again.")

        bono_locomocion = sueldo * (14 / 100)
        bono_alimentacion = sueldo * (9 / 100)

        total_locomocion += bono_locomocion
        total_alimentacion += bono_alimentacion

        print(f"CI: {ci} | Bono Locomocion: {bono_locomocion} Bs | Bono Alimentacion: {bono_alimentacion} Bs")

    print("\n********Resumen Total********")
    print(f"Se gasto en total {total_locomocion} por Conceptos de Locomocion")
    print(f"Se gasto en total {total_alimentacion} por Conceptos de Alimentacion")

print("********Bonos de Trabajadores**********")
n = int(input("Introduzca el numero de trabajadores: "))
calcular_bonos(n)