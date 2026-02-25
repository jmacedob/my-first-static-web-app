for i in range(0, 25):
    print(i)
    print("INICIAMOS...")
for i in [1,2,3,4,5]:
    print("hola", end="")
    print()
    print("finalizamos" )

for i in "betancourt":
    print(i)
    #progrma con un acmuludaror
suma = 0
for i in range(1, 11):
    suma += i   
print(f"La suma de los números del 1 al 10 es: {suma}")


        #program de numero perfecto
num = int(input("Introduce un número entero: "))
suma_divisores = 0  
for i in range(1, num):
    if num % i == 0:
        suma_divisores += i     
if suma_divisores == num:
    print(f"{num} es un número perfecto.")          
else:
    print(f"{num} no es un número perfecto.")             



          # definicion de una funcino en pytion 
    def saludo():
        print   ("Hola, bienvenido a Python!")
saludo()    
saludo()
saludo()
saludo()

                        