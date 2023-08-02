import formaciones, os
FORMACIONES = (4-3-3, 3-4-3, 4-4-2, 5-3-2)
plantillas = { 
    "Boca Juniors": formaciones.jugadores_boca_juniors,
    "River Plate": formaciones.jugadores_river_plate,
    "Independiente": formaciones.jugadores_independiente,
    "Racing": formaciones.jugadores_racing,
    "San Lorenzo": formaciones.jugadores_san_lorenzo,
    "Rosario Central": formaciones.jugadores_rosario_central,
    "Argentinos Juniors": formaciones.jugadores_argentinos_juniors,
    "Lanus": formaciones.jugadores_lanus,
    "Belgrano": formaciones.jugadores_belgrano,
    "Estudiantes de la Plata": formaciones.jugadores_estudiantes,
   
}
NOMBRE = str(input("introduzca el nombre del equipo  "))

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def buscar_jugador(plantilla):
    nombre = input("Ingrese el nombre del jugador: ")
    for jugador in plantilla:
        if jugador.nombre.lower() == nombre.lower():
            return jugador
    return None


def menu():
    while True:
        print("bienvenidos a ", NOMBRE)
        print("--")
        print("1. quieres elegir una formacion:")
        print("2. Salir")
        print("3. diccionario de jugadores")

        
        opcion = input("Ingrese una opción: ")
        FORMACIONES = [433,343,442,532]
        clear()
        if opcion == "1":
            
            print ("1; 4-3-3")
            print ("2; 3-4-3")
            print ("3; 4-4-2")
            print ("4; 5-3-2")
            opcion = input("ingrese una opcion: ")
            if opcion == "1":

                    jugadores_e = []
                    nombre_arquero = input('Escriba el nombre de su arquero > ')
                    jugadores_e.append(nombre_arquero)

                    primer_config =int(str(FORMACIONES[0])[0])

                    print(primer_config)

                    for i in range(primer_config):
                        n_jugadpr = input("escriba el nombre de un jugador > ")
                        jugadores_e.append(n_jugadpr)

                    primer_config2 =int(str(FORMACIONES[0])[1])

                    for i in range(primer_config2):
                        n_jugadpr2 = input("escriba el nombre de un jugador > ")
                        jugadores_e.append(n_jugadpr2)

                    primer_config3 =int(str(FORMACIONES[0])[2])

                    for i in range(primer_config3):
                        n_jugadpr3 = input("escriba el nombre de un jugador > ")
                        jugadores_e.append(n_jugadpr3)

                    print(jugadores_e)

        if opcion == "3":
                print("1. jugadores de boca juniors")
                print("2. jugadores de river plate")
                print("3. jugadores de independiente")
                print("4. jugadores de racing")
                print("5. jugadores de san lorenzo")
                print("6. jugadores de rosario central")
                print("7. jugadores de argentino juniors")
                print("8. jugadores de lanus")
                print("9. jugadores de belgrano")
                print("10. jugadores de estudiantes de la plata")
                op = input("ingrese una opcion: ")
                
                if op == "1":
                    print("los jugadores de boca son:'")
                    print(formaciones.jugadores_boca_juniors)
                elif  op == '2':
                      print("los jugadores de river son: ")
                      print(formaciones.jugadores_river_plate)
                elif op == "3":
                            print("los jugadores de independiente son: ")
                            print(formaciones.jugadores_independiente)
                elif op == "4":
                            print("los jugadores de racing son :")
                            print(formaciones.jugadores_racing)
                elif op == "5":
                            print("estos son los jugadores de san lorenzo: ")
                            print(formaciones.jugadores_san_lorenzo)
                elif op == "6:":
                            print("los jugadores de  rosario central son: ")
                            print(formaciones.jugadores_rosario_central)
                elif op == "7":
                            print("los jugadores de argentinos juniors son: ")
                            print(formaciones.jugadores_argentinos_juniors)
                elif op == "8":
                            print("los jugadores de lanus son :")
                            print(formaciones.jugadores_lanus)
                elif op == "9":
                            print("los jugadores de belgrano son: ")
                            print(formaciones.jugadores_belgrano)
                elif op == "10":
                            print("los jugadores de estudiantes de la plata son: ")
                            print(formaciones.jugadores_estudiantes)
                else: 
                            print('Opcion Invalida')

            
                
        
menu()