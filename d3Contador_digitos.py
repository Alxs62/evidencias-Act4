#contador de digitos
num=int(input("numero entero:"))
if num==0:
    digitos=1
else:
    digitos=0
    num=abs(num)
    while num>0:
        num//=10
        digitos+=1
print("el numero tiene",digitos,"digitos")