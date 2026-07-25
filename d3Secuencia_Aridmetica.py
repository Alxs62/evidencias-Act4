#secuencia aritmetica
inicio=int(input("ingrese el primer numero:"))
diferencia=int(input("ingrese la diferencia:"))
limite=int(input("ingrese el limite:"))
num=inicio
while True:
    print(num, end=" ")
    num+=diferencia
    if num>limite:
        break
print("\nsecuencia aritmetica desde",inicio,"hasta",limite)