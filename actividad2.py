import os

class Persona():
    def __init__(self):
        self.nombre= ""
        self.apellido = ""
        self.sexo = ""
        self.telefono = ""
        self.DicPersona = {}
        self.ListaPersona = []
    
    def agregar(self):
        self.contador = 0
        print("Agregar persona")
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.sexo = input("Sexo(M/F): ")
        self.telefono=input("Telefono: ")
        self.ListaPersona =[self.nombre, self.apellido, self.sexo, self.telefono]
        
        if len(self.DicPersona) == 0:
            self.DicPersona[1]= self.ListaPersona
        else:
            self.contador = len(self.DicPersona) +1
            self.DicPersona[self.contador]= self.ListaPersona
    
    def eliminar(self):
        self.cod = int(input("Ingrese codigo:"))
        print(self.DicPersona[self.cod])
        del self.DicPersona[self.cod]
        print("Registro borrado")

    def mostrar(self):
        print("Lista de personas")
        self.item = self.DicPersona.items()
        for co, per in self.item:
            print(co,per)
        input("Presiones cualquier tecla")

class Empleado(Persona):
    """ Constructor de la clase empleado"""
    def __init__(self):
        super().__init__()
        self.cargo = ""
        self.salario = 0

        self.DicEmpleado = {}
        self.ListaEmpleado = []

    def agregar(self):
        self.contador = 0
        print("Agregar empleado")
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.sexo = input("Sexo(M/F): ")
        self.telefono=input("Telefono: ")
        self.cargo=input("Cargo: ")
        self.salario=input("Salario: $")
        self.ListaEmpleado =[self.nombre, self.apellido, self.sexo, self.telefono, self.cargo, self.salario]
        
        if len(self.DicEmpleado) == 0:
            self.DicEmpleado[1]= self.ListaEmpleado
        else:
            self.contador = len(self.DicEmpleado) +1
            self.DicEmpleado[self.contador]= self.ListaEmpleado
    
    def eliminar(self):
        self.cod = int(input("Ingrese codigo:"))
        print(self.DicEmpleado[self.cod])
        del self.DicEmpleado[self.cod]
        print("Registro borrado")

    def mostrar(self):
        print("Lista de personas")
        self.item = self.DicEmpleado.items()
        for co, per in self.item:
            print(co,per)
        input("Presiones cualquier tecla")

def clear():
    os.system("clear")

def menu():
    objP = Persona()
    objE = Empleado()
    salida = 1
    while salida != 7 and salida>0:
        print("    Menu")
        print("1. Agregar persona.")
        print("2. Eliminar persona.")
        print("3. Mostrar persona.")
        print("4. Agregar empleado.")
        print("5. Eliminar empleado.")
        print("6. Mostrar empleado.")
        print("7. Salir")
        salida=int(input(": "))
        if salida == 1:
            clear()
            objP.agregar()
        elif salida == 2:
            clear()
            objP.eliminar()
        elif salida == 3:
           clear()
           objP.mostrar()
        elif salida == 4:
           clear()
           objE.agregar()
        elif salida == 5:
           clear()
           objE.eliminar()
        elif salida == 6:
           clear()
           objE.mostrar()
        elif salida == 7:
           break
        else:
            continue


def main():
   menu() 

if __name__ == "__main__":
    main()    
