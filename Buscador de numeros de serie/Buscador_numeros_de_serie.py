import os,re,datetime,time,math

def ruta():
    rutas="F:\Carpeta David\Trabajos U\Curso de Udemy Py\Proyectos\Buscador de numeros de serie\Proyecto9\Mi_Gran_Directorio"
    return rutas

def fecha_now():
    fecha_actual = datetime.datetime.now().date()
    return(f"Fecha de búsqueda: {fecha_actual.day}/{fecha_actual.month}/{fecha_actual.year}")

def inicio():
    ini=time.time()
    lista=[]
    print("***************************")
    print(f"{fecha_now()}\n")
    print('ARCHIVO		NRO. SERIE')
    print("***************************")
    for carpeta,subcarpeta,archivo in os.walk(ruta()):
        for arch in archivo:
            patron=r'N\D{3}-\d{5}'
            archivo = open(f'{carpeta}\{arch}', "r")
            busqueda=re.finditer(patron,archivo.read())
            for localizar in busqueda:
                if localizar:
                    lista.append(localizar)
                    print(f'{arch}\t{localizar.group()}')
    fin=time.time()
    tiempo=math.ceil(fin-ini)
    print(f"\nNumeros encontrados: {len(lista)}")
    print(f"Duración de la búsqueda: {tiempo} segundos")
    print("***************************")
    
inicio()