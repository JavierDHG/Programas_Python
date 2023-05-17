def Perfumeria():
    for x in range (1,10000):
        yield f'P- {x}'
def Medicamentos():
    for x in range (1,10000):
        yield f'M- {x}'
def Cosmeticos():
    for x in range (1,10000):
        yield f'C- {x}'

p=Perfumeria()
m=Medicamentos()
c=Cosmeticos()

def decorar(turn):
    print("Su turno es:")
    if turn=='1':
        print(next(p))
    elif turn=='2':
        print(next(m))
    elif turn=='3':
        print(next(c))
    print("Espere a su llamado, agradecemos su espera")
