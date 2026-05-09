import random

def calculadora(num1, num2, operador):
    if(operador=='+'):
        return num1+num2
    if(operador=='-'):
        return num1-num2
    if(operador=='*'):
        return num1*num2
    if(operador=='/'):
        if(num2!=0):
            return num1/num2
        else: return f'no se puede dividir entre {num2}'
    else: return 'Error'

def aleatorios(n):
    count = 0
    pares = ""
    impares = ""
    while count < n:
        numero = random.randint(1,100)
        if numero % 2 == 0:
            pares += f"{numero}, "
        else:
            impares += f"{numero}, "
        count +=1
    return f"Pares: {pares}\nImpares: {impares} "

def mayormenor(a, b, c):
    mayor=a
    menor=a
    if(a > b and a > c):
        mayor=a
    elif(b > a and b > c):
        mayor=b
    else: 
        mayor=c
    if(a < b and a < c):
        menor=a
    elif(b < a and b < c):
        menor=b
    else: 
        menor=c
    return f"Menor: {menor} Mayor: {mayor}"

opcion = ""
while opcion != '5':
    print("\n********MENU INTERACTIVO :v **********")
    print("1. Sumar numeros")
    print("2. Restar numeros")
    print("3. Multiplicar numeros")
    print("4. Dividir numeros")
    print("5. Salir")
    print("**********************************")
    print("Elija una opcion: ")
    opcion = input()

    if opcion == '1':
        print("Introduzca el primer numero: ")
        num1 = float(input())
        print("Introduzca el segundo numero: ")
        num2 = float(input())
        print(f"El resultado es: {calculadora(num1, num2, '+')}")

    elif opcion == '2':
        print("Introduzca el primer numero: ")
        num1 = float(input())
        print("Introduzca el segundo numero: ")
        num2 = float(input())
        print(f"El resultado es: {calculadora(num1, num2, '-')}")

    elif opcion == '3':
        print("Introduzca el primer numero: ")
        num1 = float(input())
        print("Introduzca el segundo numero: ")
        num2 = float(input())
        print(f"El resultado es: {calculadora(num1, num2, '*')}")

    elif opcion == '4':
        print("Introduzca el primer numero: ")
        num1 = float(input())
        print("Introduzca el segundo numero: ")
        num2 = float(input())
        print(f"El resultado es: {calculadora(num1, num2, '/')}")

    elif opcion != '5':
        print("Opcion invalida. TONTO/a solo hay 5 opciones damn.")

print("Saliendo del programa... ¡CHAU SORRITA!")