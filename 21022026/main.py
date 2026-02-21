
def sumar(a,b):
    resultado = a + b
    return resultado

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if (b == 0):
        return "No se puede dividir por cero"
    return a / b


def pedir_numero():
   correcto = True
   while (correcto):

     try:
        num1= int(input("Dame el primer número: "))
        num2=int(input("Dame el segundo número: "))
        correcto = False
        return num1, num2
    
     except ValueError:
        print("Debes ingresar un número ")
    
def pedir_un_numero():
    while True:
        try:
            num = int(input("Dame el número: "))
            return num
        except ValueError:
            print("Debes ingresar un número entero.")

def es_par(n):
    return n % 2 == 0
    

continuar = True
while (continuar):
    print("Bienvenido a la calculadora, selecciona la operación que deseas realizar")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Salir")
    print("6. Identificar si un número es par")

    try:
        opcion = int(input ("¿Qué operacion deseas realizar? Ingresa el número "))
    except ValueError:
        print("Ingresa un número válido para la opción.")
        continue

    match opcion:
        case 1:
            numero, numero2 = pedir_numero()
            print(f"La suma es: {sumar(numero, numero2)}")
        case 2:
            numero, numero2 = pedir_numero()
            print(f"La resta es: {restar(numero, numero2)}")
        case 3:
            numero, numero2 = pedir_numero()
            print(f"La división es: {dividir(numero, numero2)}")
        case 4:
            numero, numero2 = pedir_numero()
            print(f"La multiplicación es: {multiplicar(numero, numero2)}")
        case 5:
            continuar = False
            break
        case 6:
            numero = pedir_un_numero()
            if es_par(numero):
                print(f"El número {numero} es par.")
            else:
                print(f"El número {numero} es impar.")
        case _:
            print("Selecciona una opcion correcta")
    
