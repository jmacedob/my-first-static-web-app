# Programa que se ejecuta mientras se introduzcan números negativos

numero = int(input("Introduce un número: "))

while numero < 0:
    print(f"Número negativo: {numero}")
    numero = int(input("Introduce otro número: "))

print(f"¡Número no negativo ingresado! {numero}. Programa finalizado.")
