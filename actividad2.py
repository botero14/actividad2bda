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
    

    import os

def menu():
    os.system('clear')
    print ("Agregar persona")
    print ("Eliminar persona")
    print ("Mostrar persona")
    print ("Agregar empleado")
    print ("Eliminar empleado")
    print ("Mostrar empleado")
    print ("Salir")

while True: 
  
    menu()
    opcionMenu = input("¿adonde desea ir? ==> ")

    if opcionMenu =='1': 
      print ("agregar") 
    if opcionMenu == '2': 
      print ("eliminar")
    if opcionMenu == '3':
      print ("mostrar") 
    if opcionMenu == '3':
      print ("agregar")  
    if opcionMenu == '3':
      print ("eliminar") 
    if opcionMenu == '3':
      print ("mosntrar")      
    if opcionMenu == '7': 
      break
    else: 
      print ("Opcion invalida")
  

def main():
    objP = Persona()
    objE = Empleado()


    objE.agregar()
    objE.mostrar()
      


if __name__ == "__main__":
    main()    
