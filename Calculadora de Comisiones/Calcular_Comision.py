#Deivid
#02/08/2022

nombre = input("Cual es su nombre: ")
ventas = float(input("Cuanto has vendido este mes: "))
comision = ventas * 13 / 100

print(f"{nombre} ha ganado este mes {round(comision,2)}")