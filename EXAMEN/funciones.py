import random



def sueldosAleatorios(trabajadores):  
    sueldo_Aleatorio = []
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldo_Aleatorio[trabajador]= sueldo
    print("Sueldo generado aleatoriamente con exito")
    print(sueldo_Aleatorio)
    return sueldo_Aleatorio


        