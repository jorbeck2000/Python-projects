
def precio_s_descuento(ts,cant):
	if ts=="B":
		precio=700*cant
	elif ts=="E":
		precio=900*cant
	else:
		precio=1500*cant
	return precio
	
def precio_c_descuento(tc,precio):
	if tc=="F":
		descuento=precio*0.20
	else:
		if precio>=10000 and precio<20000:
			descuento=precio*0.10
		elif precio>=20000:
			descuento=precio*0.15
		else:
			descuento=0
	return descuento
	
	
def main():
	ts=input("Tipo silla: B, E, L: ")
	cant=int(input("Numero de silla: "))
	tc=input("Tipo Cliente: F, N: ")
	precio2=precio_s_descuento(ts,cant)
	descuento2=precio_c_descuento(tc,precio2)
	p3=precio2-descuento2
	
	print(precio2)
	print(descuento2)
	print(p3)

main()
			
			
