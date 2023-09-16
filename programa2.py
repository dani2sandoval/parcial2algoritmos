def cuadrado(valor):
    cuadrado = valor ** 2
    print("El cuadrado de", valor, "es:", cuadrado)

def resultado():
    x = int(input("Ingrese el primer valor: "))
    y = int(input("Ingrese el segundo valor: "))
    resultado = x * y
    print("El producto de", x, "y", y, "es:", resultado)

cuadrado(8)

resultado()
