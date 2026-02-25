peso = float(input("Ingresa tu peso en kilos: "))   
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
if imc < 18.5:  
    print("Tienes bajo peso.")      
elif 18.5 <= imc < 25:  
    print("Tienes un peso normal.") 
elif 25 <= imc < 30:  
    print("Tienes sobrepeso.")      
else:  
    print("Tienes obesidad.")   

                