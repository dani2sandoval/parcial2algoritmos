def contador(cadena):
    cadena = cadena.upper()
    
    cantidad = cadena.count('A')
    return cantidad


cadena2 = input("Ingresa cualquier texto:")


resultado = contador(cadena2)

print("Cantidad de letras a o A: ", resultado)
