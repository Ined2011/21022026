def numero_par(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return "Ambos números son pares"
    elif a % 2 == 0:
        return f"{a} es par y {b} es impar"
    elif b % 2 == 0:
        return f"{b} es par y {a} es impar"
    else:
        return "Ambos números son impares"
    
def es_par(n):
    return n % 2 == 0