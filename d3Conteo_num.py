#Conteo de numeros
n = int(input("Cantidad de numeros a ingresar: "))
mayores = 0
menores = 0
iguales = 0
for i in range(n):
    numero = float(input("Ingrese un número: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
print("Cantidad de números mayores a cero:", mayores)
print("Cantidad de números menores a cero:", menores)
print("Cantidad de números iguales a cero:", iguales)
