class Vehiculo():
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print(f"El vehículo es de tipo: {self.tipo}, marca: {self.marca}, modelo: {self.modelo}")

vehiculos = []

def agregar_vehiculo(tipo, marca, modelo):
    vehiculo = Vehiculo(tipo, marca, modelo)
    vehiculos.append(vehiculo)

def menu():
    while True:
        opcion = int(input("¿Qué desea hacer?\n"
                           "1. Agregar vehículo\n"
                           "2. Mostrar vehículos\n"
                           "3. Salir\n"
                           "Ingrese el número de la opción: "))

        if opcion == 1:
            tipo = input("Tipo: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            agregar_vehiculo(tipo, marca, modelo)
            print("El vehiculo se agrego")

        elif opcion == 2:
            if not vehiculos:
                print("No hay vehículos en la lista")
            else:
                for vehiculo in vehiculos:
                    vehiculo.mostrar_informacion()
        elif opcion == 3:
            print("Hasta luego")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()

