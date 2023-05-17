from pathlib import Path
import os
from os import remove
import shutil
from os import system

# Funciones
def direct():
    dir=(f"F:\Carpeta David\Trabajos U\Curso de Udemy Py\Recetario\Recetas")
    return dir

def crear_txt(name,name1):
    arch1=open(f'F:\Carpeta David\Trabajos U\Curso de Udemy Py\Recetario\Recetas\{name}\{name1}','w')
    Ireceta=input("Escriba la receta\n")
    arch1.write(Ireceta)
    arch1.close()

def ubicacion_docs(ubicacion):
    dir=(f"F:\Carpeta David\Trabajos U\Curso de Udemy Py\Recetario\Recetas\{ubicacion}")
    return dir

def abrir_leer(name,name1):
    archivo = open(f'F:\Carpeta David\Trabajos U\Curso de Udemy Py\Recetario\Recetas\{name}\{name1}','r')
    return archivo.read()

def crear_carpeta(nameC):
    os.makedirs(f"F:\Carpeta David\Trabajos U\Curso de Udemy Py\Recetario\Recetas\{nameC}")

def delete_txt(name,name1):
    remove(f'F:\Carpeta David\Trabajos U\Curso de Udemy Py\Recetario\Recetas\{name}\{name1}')

init=False
while init== False:
    opcion=input(' **** Escoga una opción:  **** \n1.Leer receta.\n2.Crear una receta. \n3.Crear una nueva categoria. \n4.Eliminar una receta. \n5.Eliminar categoria. \n6.Finalizar Ejecución.\n')
    # Opción 1
    if (opcion=='1'):
        # Se muestran las carpetas de la categoria de comida
        conten = os.listdir(direct())
        print(conten)
        choice=input("Escoga una categoria\n")
        # Se muestran las recetas de la categoria
        doc_zone=ubicacion_docs(choice)
        conten = os.listdir(doc_zone)
        print(conten)
        # Se selecciona la receta para leer
        choice1=input("Escoga una receta para leer\n")
        leer=abrir_leer(choice,f'{choice1}.txt')
        print(leer)
        #system("cls")

    # Opción 2
    elif (opcion=='2'):
        # Se muestran las carpetas de la categoria de comida
        conten = os.listdir(direct())
        print(conten)
        choice=input("Escoga una categoria\n")
        # Se crea un txt y su contenido
        doc_zone=ubicacion_docs(choice)
        choiceR=input("Nombre de la receta\n")
        txt = crear_txt(choice,f"{choiceR}.txt")
        #system("cls")

    # Opción 3
    elif (opcion=='3'):
        # Se digita el nombre de la categoria nueva
        Cname=input("Digite el nombre de la categoria a crear\n")
        dir=crear_carpeta(Cname)
        #system("cls")

    # Opción 4
    elif (opcion=='4'):
        conten = os.listdir(direct())
        print(conten)
        choice=input("Escoga una categoria\n")
        doc_zone=ubicacion_docs(choice)
        conten = os.listdir(doc_zone)
        print(conten)
        Dtxt=input("Digite la receta a eliminar\n")
        dir=delete_txt(choice,f"{Dtxt}.txt")
        #system("cls")

    # Opción 5
    elif (opcion=='5'):
        conten = os.listdir(direct())
        print(conten)
        choice=input("Escoga una categoria a eliminar\n")
        doc_zone=ubicacion_docs(choice)
        shutil.rmtree(doc_zone)
        #system("cls")

    # Opción 6
    elif (opcion=='6'):
        print(' **** Saliendo del menu  ****')
        init=True
    else:
        print('No existe la opcion')