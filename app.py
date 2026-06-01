def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir para cero"
    return a / b

if __name__ == "__main__":
    print("Aplicación ejercicio:3.0.0")
    print("Calculadora simple")
    print("Suma de 5 + 3 =", sumar(5, 3))