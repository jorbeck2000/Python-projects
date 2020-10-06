def piramide(altura):
    for i in range(1,altura+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print (" ")

altura=int(input("Altura: "))
piramide(altura)


def piramide_inv(altura):
    for i in range(altura+1,0,-1):
        for j in range(0,i-1):
            print("*",end=" ")
        print (" ")

altura=int(input("Altura: "))
piramide_inv(altura)

def flecha(altura):
    for i in range(1,altura+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print (" ")
    for i in range(altura+1,0,-1):
        for j in range(0,i-1):
            print("*",end=" ")
        print (" ")

altura=int(input("Altura: "))
flecha(altura)


