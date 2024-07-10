import funciones as fn

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez””Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"] 

generarSueldos = []

while True:
    print("0. Inicializar los sueldos")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    resp = int(input("Ingrese opción: "))

    if resp == 0:
        generarSueldos = {trabajador: 0 for trabajador in trabajadores}
        print("Sueldos inicializados")

    elif resp == 1:
        if generarSueldos:
            generarSueldos = fn.sueldosAleatorios(trabajadores)
        else:
            print("Debe inicializar los sueldos primero")


