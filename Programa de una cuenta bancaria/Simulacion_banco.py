# Clases
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, num_cuenta, saldo_actual=0):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.saldo_actual = saldo_actual

    def depositar(self, dinero_ingresado):
        self.saldo_actual += dinero_ingresado
        print("Deposito exitoso")

    def retirar(self, dinero_retirado):
        if self.saldo_actual > dinero_retirado:
            self.saldo_actual -= dinero_retirado
            print("Retiro exitoso")
        else:
            print("Fondos insuficientes")

    def __str__(self):
        return f'Nombre cliente: "{self.nombre} {self.apellido}", Numero cuenta: {self.num_cuenta}, Saldo total: ${self.saldo_actual}.'

# Funciones


def crear_cliente():
    nombre = input("Ingrese el nombre del cliente:\n")
    apellido = input("Ingrese el apellido del cliente:\n")
    num_cuenta = input("Ingrese el numero de su cuenta:\n")
    cliente = Cliente(nombre, apellido, num_cuenta)
    return cliente


def inicio():
    init = False
    clientes = crear_cliente()
    print(clientes)
    while init == False:
        opcion = input(' **** Escoga una opción:  **** \n1.Depositar.\n2.Retirar. \n3.Salir.\n')
        # Depositar dinero
        if (opcion == '1'):
            depositos = int(input("Digite la cantidad a depositar.\n"))
            clientes.depositar(depositos)
            print(str(clientes))
        # Retirar dinero
        elif (opcion == '2'):
            retiros = int(input("Digite la cantidad a retirar.\n"))
            clientes.retirar(retiros)
            print(str(clientes))
        # Terminar ejecucion
        elif (opcion == '3'):
            print(' **** Saliendo del menu  ****')
            init = True
        else:
            print('No existe la opcion')


inicio()
