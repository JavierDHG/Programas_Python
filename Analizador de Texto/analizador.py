#Deivid
#02/08/2022

txt = input("Ingrese cualquier texto\n")
letra1 = input("Ingrese cualquier letra\n")
letra2 = input("Ingrese cualquier letra\n")
letra3 = input("Ingrese cualquier letra\n")
lista = [letra1,letra2,letra3]
orgnztxt = txt.lower()
listtxt = list(orgnztxt)
palabras = orgnztxt.split()

print("\n")
print(f"La letra {letra1} aparece {orgnztxt.count(lista[0])},La letra {letra2} aparece {orgnztxt.count(lista[1])},La letra {letra3} aparece {orgnztxt.count(lista[2])}")

print(f"Existen {len(palabras)} palabras en total")

print(f"{listtxt[0]} es la primera palabra, {listtxt[-1]} es la primera palabra")

palabras.reverse()
txtinver = ' '.join(palabras)
print(f"Este seria el texto inverso\n{txtinver}")

buscar_palabra = "python" in orgnztxt
dic = {True:"si",False:"no"}
print(f"La palabra 'Python' {dic[buscar_palabra]} se encuentra en el texto")