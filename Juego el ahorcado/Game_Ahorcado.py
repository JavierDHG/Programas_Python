import random

# Se solicita la letra al usuario
def pedir_letra():
    letra = input("Ingrese una letra de la a hasta la z\n") #Se ingresa la letra de la a-z
    return letra.lower() #Convierte todo lo ingresado en minuscula

# Se valida si la entrada que dio el usuario es una letra
def validar_letra(vletra):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z'] #Lista de letras para validar ingreso de usuario
    if vletra in letras: #Se valida si la letra ingresada se encuentra en la lista
        return vletra #Si es asi, retorna la letra
    elif vletra not in letras: #Si la letra ingresada no se encuentra en la lista, entonces ingresa a un ciclo while
        while vletra not in letras: #Mientras la letra ingresada no este en la lista, el ciclo funcionara hasta ingresar una letra correcta
            vletra = input("No se ha dijitado una letra, ingrese una letra de la a hasta la z\n") #Se pide de nuevo una letra
            if vletra in letras: #Si la letra ingresada en el ciclo while, se encuentra en la lista, entonces 
                break #se rompe el ciclo y 
    return vletra #devuelve la letra ya validada

# Se valida si la letra dada, esta en la frase
def chequear_letra(letra,frase,vidas): #Se recibe la la letra validada y la frase escogida aleatoriamente de una lista
    fin =False
    frase_completa=[] #Se crea una lista, para almacenar el tamaño de la frase con raya al piso
    if vidas==0:
        fin= sinvidas()
    elif letra not in frase:
        vidas -= 1
        print(f"Sus vidas son {vidas}")
    else:
        pass  
    for pos,valor in enumerate(frase): #Se crea un for para recorrer la frase y saber su tamaño y su contenido
        frase_completa.append('_') #Segun el tamaño, se agregan raya al piso, para saber el tamaño de la frase   
        if letra in valor: #Si la letra se encuentra en la frase, se hace lo siguiente
            frase_completa[pos]=letra #En la posicion dada, se escribe la letra que si se encuentra en esa posicion
 
    print(frase_completa)
    return vidas,fin,frase_completa

def sinvidas():
    print("Ya se han agotado las vidas")

vidas=6
frases=['casa','carro','new york','colegio','muñeco']
frase_ale=random.choice(frases)
print(frase_ale)
letra_ing = pedir_letra()
letra_validada=validar_letra(letra_ing)
chequear_letra(letra_validada,frase_ale,vidas)