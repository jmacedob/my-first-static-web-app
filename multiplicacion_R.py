def multiplicacion_rusa(a, b):
    """
    Implementa el algoritmo de multiplicación rusa.
    Multiplica dos números usando el método de duplicación y mediación.
    """
    resultado = 0
    
    while a > 0:
        # Si a es impar, sumamos b al resultado
        if a % 2 == 1:
            resultado += b
        
        # Dividimos a entre 2 (mediación) y duplicamos b
        a //= 2
        b *= 2
    
    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    num1 = 25
    num2 = 32
    
    resultado = multiplicacion_rusa(num1, num2)
    print(f"{num1} × {num2} = {resultado}")