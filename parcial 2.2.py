
s=int(input("Cantidad de veces: "))
sumapar=0
sumaimpar=0
impar=0
par=0
for i in range (1,s+1):
    num=int(input("Número: "))

    if num%2==0:
        par=par+1
        sumapar=num+sumapar
        promediop=sumapar/par

    else:
        impar=impar+1
        sumaimpar=num+sumaimpar
        promedioi=sumaimpar/impar

print("Cantidad de pares: ", par )
print("Cantidad de impares: ", impar)

print("Suma pares: ",sumapar)
print("Suma impares: ", sumaimpar)

print("promedio pares: ",promediop)
print("Promedio impares: ", promedioi)





