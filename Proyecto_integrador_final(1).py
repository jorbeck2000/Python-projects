import random
import sys
cont1=0
cont2=0

nombre=str(input("Nombre del jugador 1: "))
nombre2=str(input("Nombre del jugador 2: "))
resp=str(input("¿Deseas ver la hoja de respuestas?: si/no "))
valores = ['01 ','01 ', '02 ', '02 ','03 ','03 ','04 ','04 ','05 ','05 ','06 ','06 ','07 ','07 ','08 ','08 ','09 ','09 ','10 ','10 ','11 ','11 ','12 ','12 ','13 ','13 ','14 ','14 ','15 ','15 ','16 ','16 ','17 ','17 ','18 ','18 ']
random.shuffle(valores) #randomize todas las fichas#
valores = [valores[:6],#Agrupa las posib en juegos de 4 para hace el tablero#
         valores[6:12],
         valores[12:18],
         valores[18:24],
           valores[24:30],
           valores[30:36]]

print("Aqui podrás ver las coordenadas de cada una de las posibles selecciones")

coordenadas=[["00 ","01 ","02 ","03 ","04 ","05 "],#Imprime un mapa de las coordenadas del tablero#
             ["10 ","11 ","12 ","13 ","14 ","15 "],
             ["20 ","21 ","22 ","23 ","24 ","25 "],
             ["30 ","31 ","32 ","33 ","34 ","35 "],
             ["40 ","41 ","42 ","43 ","44 ","45 "],
             ["50 ","51 ","52 ","53 ","54 ","55 "]]

def imprimir(coordenadas):
    for i in coordenadas:
        for j in i:
            print(j, end=" ")
        print()
imprimir(coordenadas)

if resp=="si":#Si decides que quieres ver las respuestas escribes si y se abre un mapa con respuestas#
    print("Hoja de respuestas")
    def imprimir(valores):
        for i in valores:
            for j in i:
                print(j, end=" ")
            print()
    imprimir(valores)


    

tablero = [list('█'*6) for i in range(6)] #for que dibuja el tablero, crea matriz de █#



def eleccion():
    global cont1
    global cont2
    a,b = map(int, input('Primera elección del jugador 1: '))#Solicita coordenadas de primera elección# #la funcion map hace que busque en el tablero la coordenada seleccionada#
    mostrar_tablero((a,b))#coordenadas de la primera elección#
    x,y = map(int, input('Segunda elección del jugador 1: '))#Coordenanas de la segunda elección#
    mostrar_tablero((a,b),(x,y))#Muestra las 2 elecciones para evaluar si son iguales#
    if valores [a][b] == valores[x][y]: #evalua si la primera y la segunda opcion son iguales#
        print('Eres buenísimo/a',nombre, '¡ Si son iguales!!')
        cont1+=1
        print("Tu puntaje es: ", cont1,"pares" )
        romper=str(input("¿Quieres seguir jugando? "))
        if romper == "no":
            print("Fin del juego")
            print("El marcador fue: ",nombre, "-", cont1, " ", nombre2, "-", cont2)
            sys.exit("Fin del programa")   
        tablero[a][b] = valores[a][b]#Si la primera y segunda eleccion son iguales se mantienen abiertas#
        tablero[x][y] = valores[x][y]
    else:
        print('¿Qué pasa' ,nombre,'? sigue intentando.')
        print("Tu puntaje es: ", cont1, "pares")
        romper=str(input("¿Quieres seguir jugando?: si/no "))
        if romper=="no":
            print("Fin del juego")
            print("El marcador fue: ",nombre, "-", cont1, " ", nombre2, "-", cont2)
            sys.exit("Fin del programa")

    a,b = map(int, input('Primera elección del jugador 2: '))#Solicita coordenadas de primera elección# #la funcion map hace que busque en el tablero la coordenada seleccionada#
    mostrar_tablero((a,b))#coordenadas de la primera elección#
    x,y = map(int, input('Segunda elección del jugador 2: '))#Coordenanas de la segunda elección#
    mostrar_tablero((a,b),(x,y))#Muestra las 2 elecciones para evaluar si son iguales#
    if valores [a][b] == valores[x][y]: #evalua si la primera y la segunda opcion son iguales#
        print('Eres buenísimo/a',nombre2, '¡ Si son iguales!!')
        cont2+=1
        print("Tu puntaje es: ", cont2, "pares")
        romper=str(input("¿Quieres seguir jugando?: si/no "))
        if romper == "no":
            print("Fin del juego")
            print("El marcador fué: ",nombre, "-", cont1, " ", nombre2, "-", cont2)
            sys.exit("Fin del programa")
        tablero[a][b] = valores[a][b]#Si la primera y segunda eleccion son iguales se mantienen abiertas#
        tablero[x][y] = valores[x][y]    
    else:
        print('¿Qué pasa' ,nombre2,'? sigue intentando.')
        print("Tu puntaje es: ", cont2, "pares")
        romper=str(input("¿Quieres seguir jugando?: si/no "))
        if romper == "no":
            print("Fin del juego")
            print("El marcador fue: ",nombre, "-", cont1, " ", nombre2, "-", cont2)
            sys.exit("Fin del programa")
            

    if any('█' in fila for fila in tablero):#Que el juego continue hasta que ya no hayan escondidas#
        return True
    
def mostrar_tablero(*fichas):#Acomoda el tablero en 4x4 como lo muestra variable respuesta#
    for fila in range(len(valores)): #fila de 4 valores#
        for columna in range(len(valores[0])):#Columna de 6 valores#
            if (fila,columna) in fichas:
                print(valores[fila][columna], end='')#Ocasiona que tu elección se muestre y se eliminen los █#
            else:
                print(tablero[fila][columna], end='')
        print()


    

mostrar_tablero()

while eleccion():
    pass

print('Que éxito terminaron')
print(nombre,'obtuvo: ',cont1,'  ' ,nombre2, 'obtuvo: ', cont2)
