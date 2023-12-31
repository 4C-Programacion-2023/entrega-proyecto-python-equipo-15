import formaciones, os
FORMACIONES = (4-3-3, 3-4-3, 4-4-2, 5-3-2)
plantillas = { 
    "Boca Juniors": formaciones.jugadores_de_boca,
    "River Plate": formaciones.jugadores_river,
    "Independiente": formaciones.jugadores_independiente,
    "Racing": formaciones.jugadores_racing,
    "San Lorenzo": formaciones.jugadores_san_lorenzo,
    "Rosario Central": formaciones.jugadores_rosario_central,
    "Argentinos Juniors": formaciones.jugadores_argentinos_junior,
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
        print("2. diccionario de jugadores")
        print("3. salir")

        
        opcion = input("Ingrese una opción: ")
        FORMACIONES = [433,343,442,532]
        clear()
        if opcion == "1":
            print ("1; 4-3-3")
            print ("2; 3-4-3")
            print ("3; 4-4-2")
            print ("4; 5-3-2")
            opcion = input("ingrese una opcion: ")
            clear()
            if opcion == "1":
             
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudaintes")
                a= int(input("ingrese un equipo"))
                if a == 1:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_boca_junior.keys()))
                    print("----------------------------------------------------------------------------") 
                    arquero= input("introduzca el nombre de tu arquero:  ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    print("----------------------------------------------------------------------------")                
                    defensa1= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa2= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa3= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa4= input("introduzca el nombre de tu defensor: ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo1=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo2=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo3=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_boca_delatneros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero1= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_boca_delatneros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero2= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_boca_delatneros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero3 = input("introduzca el nombre de tu delantero: ")
                elif a==2:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_river.keys()))
                    print("----------------------------------------------------------------------------")
                    arquero= input("introduzca el nombre de tu arquero:  ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa1= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa2= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa3= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa4= input("introduzca el nombre de tu defensor: ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo1=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo2=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo3=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero1= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero2= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero3= input("introduzca el nombre de tu delantero:  ")
                elif a == 3:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_racing.keys()))
                    print("----------------------------------------------------------------------------")
                    arquero= input("introduzca el nombre de tu arquero:  ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa1= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa2= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa3= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa4= input("introduzca el nombre de tu defensor: ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo1=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo2=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo3=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero1= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero2= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero3= input("introduzca el nombre de tu delantero:  ")
                elif a ==4 :
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_independiente.keys()))
                    print("----------------------------------------------------------------------------") 
                    arquero= input("introduzca el nombre de tu arquero:  ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    print("----------------------------------------------------------------------------")                
                    defensa1= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa2= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa3= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa4= input("introduzca el nombre de tu defensor: ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo1=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo2=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo3=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero1= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero2= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero3 = input("introduzca el nombre de tu delantero: ")
                elif a==5:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_san_lorenzo.keys()))
                    print("----------------------------------------------------------------------------")
                    arquero= input("introduzca el nombre de tu arquero:  ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa1= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa2= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa3= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa4= input("introduzca el nombre de tu defensor: ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo1=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo2=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo3=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero1= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero2= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero3= input("introduzca el nombre de tu delantero:  ")
                elif a==6: 
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores.keys()))
                    print("----------------------------------------------------------------------------")
                    arquero= input("introduzca el nombre de tu arquero:  ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa1= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa2= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa3= input("introduzca el nombre de tu defensor: ")
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    print("----------------------------------------------------------------------------")
                    defensa4= input("introduzca el nombre de tu defensor: ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo1=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo2=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    print("----------------------------------------------------------------------------")
                    mediocampo3=input("introduzca el nombre de tus mediocampista:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero1= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero2= input("introduzca el nombre de tu delantero:  ")
                    print("Posibles delanteros: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    print("----------------------------------------------------------------------------")
                    delantero3= input("introduzca el nombre de tu delantero:  ")
                      
            for nombre_equipo, equipo_jugadores in plantillas.items():
                print(f"Revisando el equipo: {nombre_equipo}")
                
                for jugador, info in equipo_jugadores.items():
                    if (
                        jugador == arquero or
                        jugador == defensa1 or
                        jugador == defensa2 or
                        jugador == defensa3 or
                        jugador == defensa4 or
                        jugador == mediocampo1 or
                        jugador == mediocampo2 or
                        jugador == mediocampo3 or
                        jugador == delantero1 or
                        jugador == delantero2 or
                        jugador == delantero3
                    ):
                        print(f"Equipo: {jugador} - {info}")
                        break
                else:
                    print(f"Jugador no encontrado en el equipo.")

        clear()
        if opcion == "2":
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
                clear()
                if op == "1":
                    print("los jugadores de boca son:'")
                    print("los arqueros son: ")
                    print(formaciones.jugadores_de_boca)
                    print(                                            )
                    print("los defensores son: ")
                    print(formaciones.jugadores_de_boca_defensores)
                    print(                                            )
                    print("los mediocampistas son: ")
                    print(formaciones.jugadores_de_boca_mediocampistas)
                    print (                                           )
                    print("los delanteros son:  ")
                    print(formaciones.jugadores_de_boca_delatneros)
                elif  op == '2':
                      print("los jugadores de river son: ")
                      print(                                                    )
                      print("los arqueros son: ")
                      print(formaciones.jugadores_river)
                      print(                                                      )
                      print( "los defensores son: ")
                      print(formaciones.jugadores_river_defensores)
                      print(                                                        )
                      print("los mediocampistas son: ")
                      print(formaciones.jugadores_de_river_mediocampistas)
                      print(                                                        )
                      print("los delanteros son: ")
                      print(formaciones.jugadores_de_river_delanteros)
                elif op == "3":
                            print("los jugadores de independiente son: ")
                            print(                                  )
                            print("los arqueros son:  ")
                            print(formaciones.jugadores_independiente)
                            print(                                                   )
                            print("los defensores son: ")
                            print(formaciones.jugadores_de_independiente_defensores)
                            print(                                                       )
                            print("los mediocampistas son: ")
                            print(formaciones.jugadores_de_independiente_mediocampistas)
                            print(                                                  )
                            print("los delanteros son: ")
                            print(formaciones.jugadores_de_independiente_delanteros)
                elif op == "4":
                            print("los jugadores de racing son :")
                            print(                                          )
                            print("los arqueros son:  ")
                            print(formaciones.jugadores_racing)
                            print(                                            )
                            print("los defensores son:  ")
                            print(formaciones.jugadores_racing_defensores)
                            print(                                                )
                            print("los mediocampistas son: ")
                            print(formaciones.jugadores_racing_mediocampistas)
                            print(                                                   )
                            print(" los delanteros son: ")
                            print(formaciones.jugadores_de_racing_delanteros)
                elif op == "5":
                            print("estos son los jugadores de san lorenzo: ")
                            print("                                   ")
                            print("los arqueros son:    ")
                            print(formaciones.jugadores_san_lorenzo)
                            print(                                                        )
                            print("los mediocampistas son:  ")
                            print(formaciones.jugadores_de_san_lorenzo_mediocampista)
                            print(                                                                              )
                            print("los delanteros son:  ")
                            print(formaciones.jugadores_de_san_lorenzo_delantero)
                elif op == "6:":
                            print("los jugadores de  rosario central son: ")
                            print(                                                        )
                            print("los arqueros son: ")
                            print(formaciones.jugadores_rosario_central)
                            print(                                                       )
                            print("los defensores son: ")
                            print(formaciones.jugadores_de_rosario_central_defensores)
                            print(                                                                   )
                            print("los mediocampistas son: ")
                            print(formaciones.jugadores_de_rosario_central_mediocampistas)
                            print(                                                                          )
                            print("los delanteros son: ")
                            print(formaciones.jugadores_de_rosario_central_delanteros)
                elif op == "7":
                            print("los jugadores de argentinos juniors son: ")
                            print(                                                  )
                            print("los arqueros som: ")
                            print(formaciones.jugadores_argentinos_junior)
                            print(                                                             )
                            print("los defensores son: ")
                            print(formaciones.jugadores_de_argentinos_jr_defensores)
                            print(                                                            )
                            print("los mediocampistas son: ")
                            print(formaciones.jugadores_de_argentinos_jr_mediocampistas)
                            print(                                                           )
                            print("los delanteros son: ")
                            print(formaciones.jugadores_de_argentinos_jr_delantero)
                elif op == "8":
                            print("los jugadores de lanus son :")
                            print(                                                    )
                            print("los arqueros son: ")
                            print(formaciones.jugadores_lanus)
                            print(                                                   )
                            print("los defensores son: ")
                            print(formaciones.jugadores_de_lanus_defensores)
                            print(                                                      )
                            print("los mediocampistas son:  ")
                            print(formaciones.jugadores_de_lanus_mediocampistas)
                            print(                                           )
                            print("los delanteros son: ")
                            print(formaciones.jugadores_de_argentinos_jr_delantero)
                elif op == "9":
                            print("los jugadores de belgrano son: ")
                            print(                                          )
                            print(formaciones.jugadores_belgrano)
                            print(                                              )
                            print("los defensores son:  ")
                            print(formaciones.jugadores_de_belgrano_defensores)
                            print(                                                )
                            print("los mediocampistas son:  ")
                            print(formaciones.jugadores_de_belgrano_defensores)
                            print(                                                              )
                            print( "los delanteros son:  ")
                            print(formaciones.jugadores_de_belgrano_delantero)
                            print
                elif op == "10":
                            print("los jugadores de estudiantes de la plata son: ")
                            print(                                                                 )
                            print("los arqueros son: ")
                            print(formaciones.jugadores_estudiantes)
                            print(                                                    )
                            print("los defensores son: ")
                            print(formaciones.jugadores_de_estudiantes_defensores)
                            print(                                                             )
                            print("los mediocampistas son: ")
                            print(formaciones.jugadores_de_estudaintes_mediocampistas)
                            print(                                                                          )
                            print("los delanteros son:  ")
                            print(formaciones.jugadores_de_estudiantes_delanteros)
                else: 
                            print('Opcion Invalida, intente otra vez')

            
                
        
menu()
