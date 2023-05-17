from numeros import *

#Se escoge el area
def menu_inicio():
    while True:    
        try:
            opcion = input(' **** Escoga un area:  **** \n1.Perfumeria.\n2.Medicamentos.\n3.Cosmeticos.\n')
        except ValueError:
            print("No se reciben letras")
        else:
            break
    return opcion

def instrucciones(opcion):
    eleccion=opcion
    #Perfumeria
    if (eleccion == '1'):
        decorar(eleccion)
    #Medicamentos
    elif (eleccion == '2'):  
        decorar(eleccion)
    #Cosmeticos
    elif (eleccion == '3'):  
        decorar(eleccion)

def repeticiones():
    init=False
    eleccion=menu_inicio()
    instrucciones(eleccion)
    while init==False:
        preguntar=input("Sacar siguiente turno: \n1.SI. 2.NO\n")
        if preguntar=='1':
            eleccion=menu_inicio()
            instrucciones(eleccion)
        elif preguntar=='2':
            print("Gracias por preferirnos a nosotros")
            init = True
        else:
            print("No existe la opcion")
            
repeticiones()