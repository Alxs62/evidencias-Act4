#Contador de números impares
Num = int(input("Número positivo: "))
i = 1
while True:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
    if i > Num:
        break
print("\nFin. Se mostraron los impares hasta", Num)