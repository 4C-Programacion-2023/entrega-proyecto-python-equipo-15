#trabajo de lorenzo cirrincione y facundo peralta
import os
import formaciones


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

print("Bienvenido a ArgenDream XI")
NOMBRE = str(input("introduzca el nombre del equipo: "))

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
    clear()
    while True:
        print("bienvenidos a ", NOMBRE)
        print("--")
        print("1. Elegir una formacion:")
        print("2. Diccionario de jugadores: ")
        print("3. Crear un jugador: ")
        print("4. Más acerca de ArgenDream XI: ")
        print("5. Salir: ")
        
        
        
        opcion = input("Ingrese una opción: ")
        
        FORMACIONES = [433,343,442,532]
        
        clear()
#es informacion sobre el producto
        if opcion == "4":
            clear()
            while True:
                print("¿De qué se trata nuestro juego?")
                print("ArgenDream XI te permite crear tu once soñado con jugadores de los 10 equipos más grandes de Argentina e incluso tiene un equipo con las mejores leyendas, las cuales puedes introducir en tu equipo.")
                print("También posee un diccionario en el cual puedes acceder a toda la información de tus jugadores, solo presionando la tecla 2 en el menú.")
                print("Y presionando la tecla 3 del menú, puedes crear tu propio jugador e introducirlo en tu plantilla.")
                print("Los desarrolladores de esta increíble aplicación son Facundo Peralta y Lorenzo Cirrincione. Su idea fue impulsada por un proyecto escolar en el año 2023 y terminó siendo la aplicación número 1 en aplicaciones para crear plantillas soñadas!")
                print()
                x = input("Presione 1 si quiere volver al menú: ")
                if x == "1":
                    menu()
                    break
                else:
                    print("Error!")
                    clear()
#todos los comandos utilizados para poder crear un jugador
        if opcion == "3":
            clear()

            nombrej = input("Ingrese el nombre del jugador: ")
            edadj = int(input("Ingrese la edad del jugador: "))
            posicionj = input("Ingrese la posición del jugador: ")
            valoracion = float(input("Ingrese el valoracion del jugador: "))
            clear()

            print("Jugador creado exitosamente:")
            print("Nombre:", nombrej)
            print("Edad:", edadj)
            print("Posición:", posicionj)
            print("Valoracion:", valoracion)

            jugador = {
                "nombre": nombrej,
                "edad": edadj,
                "posicion": posicionj,
                "valoracion": valoracion
            }
            print("los datos de tu jugador quedaran guardados y podran ser utilizados luego para incluir en tu plantilla")
            input("continuar > ")
            
            clear()
#para romper los bucles y terminar todo
        if opcion == "5":
            clear()
            print("Hasta pronto! Gracias por jugar ")
            break
        clear()
#todos lo comandos utilizados para poder hacer tu plantilla con los jugadores que querramos
        if opcion == "1":
            print("Eliga una formacion")
            print ("1; 4-3-3")
            print ("2; 3-4-3")
            print ("3; 4-4-2")
            print ("4; 5-3-2")
            opcion = input("ingrese una opcion: ")
            clear()
            if opcion == "1":
                clear()
                print("ingrese de que equipo quiere que sea su arquero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; arqueros leyendas")
                print("12; jugador creado")
                a= int(input("ingrese un equipo:  "))
                
                if a == 1:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_de_boca.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 2:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_river.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 3:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_racing.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 4:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_independiente.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")     
                elif a == 5:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_san_lorenzo.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 6:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_rosario_central.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")              
                elif a == 7:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_argentinos_junior.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")               
                elif a == 8:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_lanus.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 9:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_belgrano.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")             
                elif a == 10:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_estudiantes.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 11:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_leyendas_arqueros.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 12:
                    print("Posibles arquero: " + ", ", nombrej)
                    arquero = input("introduzca el nombre de tu arquero: ")
                clear()
                print("ingrese de que equipo quiere que sea su primer defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12, jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer defensorr
                if d == 1:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 11:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa1 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa2 = input("introduzca el nombre de tu segundo defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa2 = input("introduzca el nombre de tu segundo  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 12:
                   print("Posibles defensor: " + ", ", nombrej)
                   defensa2 = input("introduzca el nombre de tu defensor: ")

                clear()
                print("ingrese de que equipo quiere que sea su tercer  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa3 = input("introduzca el nombre de tu tercer defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa3 = input("introduzca el nombre de tu tercer  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")  
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa3 = input("introduzca el nombre de tu segundo defensor: ")     
                elif d == 12: 
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa3 = input("introduzca el nombre de tu defensor: ")  
                clear()
                print("ingrese de que equipo quiere que sea su cuarto defensor  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyenda")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el cuarto defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa4 = input("introduzca el nombre de tu cuarto defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")  
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa4 = input("introduzca el nombre de tu segundo defensor: ")     
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa4 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su primer mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyenda")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio1= input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 7:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistaskeys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ")  
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio1 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio12 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su tercero mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio13= input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista ")  
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu primer mediocampista ")    
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio13 = input("introduzca el nombre de tu mediocampista: ") 
                clear()
                print("ingrese de que equipo quiere que sea su primer delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero1= input("introduzca el nombre de tu delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")  
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero1 = input("introduzca el nombre de tu delantero: ") 
                clear()
                print("ingrese de que equipo quiere que sea su segundo delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:  ")  
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero12 = input("introduzca el nombre de tu delantero: ")   
                clear()
                print("ingrese de que equipo quiere que sea su tercer delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero:  ")       
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu primer delantero:  ")  
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero13 = input("introduzca el nombre de tu delantero: ") 
                clear()
                while True:
                    print("Tu equipo final quedó de la siguiente manera:")
                    print()
                    print("Arquero:")
                    print(arquero)
                    print("Defensores:")
                    print(defensa1)
                    print(defensa2)
                    print(defensa3)
                    print(defensa4)
                    print("Mediocampistas:")
                    print(medio1)
                    print(medio12)
                    print(medio13)
                    print("Delanteros:")
                    print(delantero1)
                    print(delantero12)
                    print(delantero13)
                    
                    r = input("Si quieres volver al menú, presiona (1): ")
                    if r == "1":
                        menu()
                        break
                    else:
                        print("Error!")
            elif opcion == "2":
                clear()
                print("ingrese de que equipo quiere que sea su arquero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; arqueros leyendas")
                print("12; jugador creado")
                a= int(input("ingrese un equipo:  "))
                
                if a == 1:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_de_boca.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 2:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_river.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 3:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_racing.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 4:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_independiente.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")     
                elif a == 5:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_san_lorenzo.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 6:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_rosario_central.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")              
                elif a == 7:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_argentinos_junior.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")               
                elif a == 8:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_lanus.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 9:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_belgrano.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")             
                elif a == 10:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_estudiantes.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 11:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_leyendas_arqueros.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 12:
                    print("Posibles arquero: " + ", ", nombrej)
                    arquero = input("introduzca el nombre de tu arquero: ")      
                clear()
                print("ingrese de que equipo quiere que sea su primer defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12, jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer defensorr
                if d == 1:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 11:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa1 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa2 = input("introduzca el nombre de tu segundo defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa2 = input("introduzca el nombre de tu segundo  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa2 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su tercer  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa3 = input("introduzca el nombre de tu tercer defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa3 = input("introduzca el nombre de tu tercer  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")  
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa3 = input("introduzca el nombre de tu segundo defensor: ")     
                elif d == 12: 
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa3 = input("introduzca el nombre de tu defensor: ")    
                clear()
                print("ingrese de que equipo quiere que sea su primer mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyenda")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio1= input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 7:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistaskeys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ")  
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio1 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio12 = input("introduzca el nombre de tu mediocampista: ") 
                clear()
                print("ingrese de que equipo quiere que sea su tercero mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio13= input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista ")  
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu primer mediocampista ")    
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio13= input("introduzca el nombre de tu mediocampista ") 
                clear()
                print("ingrese de que equipo quiere que sea su cuarto mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyenda")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el cuarto mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio14  = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista ")  
                elif m == 11:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista ")  
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio14 = input("introduzca el nombre de tu mediocampista: ") 

                clear()
                print("ingrese de que equipo quiere que sea su primer delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero1= input("introduzca el nombre de tu delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")  
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero1 = input("introduzca el nombre de tu delantero: ") 
                clear()
                print("ingrese de que equipo quiere que sea su segundo delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:  ")  
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero12 = input("introduzca el nombre de tu delantero: ")    
                clear()
                print("ingrese de que equipo quiere que sea su tercer delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu tercer delantero:  ")       
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero13 = input("introduzca el nombre de tu primer delantero:  ")  
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero13 = input("introduzca el nombre de tu delantero: ") 
                clear()
                clear()
                while True:
                    print("Tu equipo final quedó de la siguiente manera:")
                    print()
                    print("Arquero:")
                    print(arquero)
                    print("Defensores:")
                    print(defensa1)
                    print(defensa2)
                    print(defensa3)
                    print("Mediocampistas:")
                    print(medio1)
                    print(medio12)
                    print(medio13)
                    print(medio14)
                    print("Delanteros:")
                    print(delantero1)
                    print(delantero12)
                    print(delantero13)
                    
                    r = input("Si quieres volver al menú, presiona (1): ")
                    if r == "1":
                        menu()
                        break
                    else:
                        print("Error!")
            elif opcion == "3":
                clear()
                print("ingrese de que equipo quiere que sea su arquero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; arqueros leyendas")
                print("12; jugador creado")
                a= int(input("ingrese un equipo:  "))
                
                if a == 1:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_de_boca.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 2:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_river.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 3:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_racing.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 4:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_independiente.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")     
                elif a == 5:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_san_lorenzo.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 6:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_rosario_central.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")              
                elif a == 7:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_argentinos_junior.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")               
                elif a == 8:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_lanus.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 9:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_belgrano.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")             
                elif a == 10:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_estudiantes.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 11:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_leyendas_arqueros.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 12:
                    print("Posibles arquero: " + ", ", nombrej)
                    arquero = input("introduzca el nombre de tu arquero: ")  
                clear()  
                print("ingrese de que equipo quiere que sea su primer defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12, jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer defensorr
                if d == 1:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 11:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa1 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa2 = input("introduzca el nombre de tu segundo defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa2 = input("introduzca el nombre de tu segundo  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 12:
                   print("Posibles defensor: " + ", ", nombrej)
                   defensa2 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su tercer  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12;jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa3 = input("introduzca el nombre de tu tercer defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa3 = input("introduzca el nombre de tu tercer  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")  
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa3 = input("introduzca el nombre de tu segundo defensor: ")     
                elif d == 12: 
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa3 = input("introduzca el nombre de tu defensor: ")  
                clear()
                print("ingrese de que equipo quiere que sea su cuarto defensor  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyenda")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el cuarto defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa4 = input("introduzca el nombre de tu cuarto defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")  
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa4 = input("introduzca el nombre de tu segundo defensor: ")     
                elif d == 12:
                   print("Posibles defensor: " + ", ", nombrej)
                   defensa4 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su primer mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyenda")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio1= input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 7:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistaskeys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ")  
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio1 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio12 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su tercero mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio13= input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista ")  
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu primer mediocampista ")    
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio13 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su cuarto mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyenda")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el cuarto mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio14  = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista ")  
                elif m == 11:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio14 = input("introduzca el nombre de tu cuarto mediocampista ")  
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio14 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su primer delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero1= input("introduzca el nombre de tu delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")  
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero1 = input("introduzca el nombre de tu delantero: ") 
                clear()
                print("ingrese de que equipo quiere que sea su segundo delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:  ")  
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero12 = input("introduzca el nombre de tu delantero: ")   
                clear()
                while True:
                    print("Tu equipo final quedó de la siguiente manera:")
                    print()
                    print("Arquero:")
                    print(arquero)
                    print("Defensores:")
                    print(defensa1)
                    print(defensa2)
                    print(defensa3)
                    print(defensa4)
                    print("Mediocampistas:")
                    print(medio1)
                    print(medio12)
                    print(medio13)
                    print(medio14)
                    print("Delanteros:")
                    print(delantero1)
                    print(delantero12)
                    r = input("Si quieres volver al menú, presiona (1): ")
                    if r == "1":
                        menu()
                        break
                    else:
                        print("Error!")
            elif opcion == "4":
                clear()
                print("ingrese de que equipo quiere que sea su arquero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; arqueros leyendas")
                print("12; jugador creado")
                a= int(input("ingrese un equipo:  "))
                if a == 1:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_de_boca.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 2:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_river.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 3:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_racing.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 4:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_independiente.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")     
                elif a == 5:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_san_lorenzo.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 6:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_rosario_central.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")              
                elif a == 7:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_argentinos_junior.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")               
                elif a == 8:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_lanus.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 9:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_belgrano.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")             
                elif a == 10:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_estudiantes.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 11:
                    print("Posibles arquero: " + ", ".join(formaciones.jugadores_leyendas_arqueros.keys()))
                    arquero = input("introduzca el nombre de tu arquero: ")
                elif a == 12:
                    print("Posibles arquero: " + ", ", nombrej)
                    arquero = input("introduzca el nombre de tu arquero: ")    
                clear()  
                print("ingrese de que equipo quiere que sea su primer defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer defensorr
                if d == 1:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 11:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                    defensa1 = input("introduzca el nombre de tu primer defensor: ")
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa1 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa2 = input("introduzca el nombre de tu segundo defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa2 = input("introduzca el nombre de tu segundo  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa2 = input("introduzca el nombre de tu segundo defensor: ")
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa2 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su tercer  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa3 = input("introduzca el nombre de tu tercer defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa3 = input("introduzca el nombre de tu tercer  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa3 = input("introduzca el nombre de tu tercer defensor: ")  
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa3 = input("introduzca el nombre de tu segundo defensor: ")     
                elif d == 12: 
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa3= input("introduzca el nombre de tu defensor: ")    
                clear()
                print("ingrese de que equipo quiere que sea su cuarto defensor  defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyenda")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el cuarto defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa4 = input("introduzca el nombre de tu cuarto defensor defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu tercer defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa4 = input("introduzca el nombre de tu cuarto defensor: ")  
                elif d == 11:
                     print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                     defensa4 = input("introduzca el nombre de tu segundo defensor: ")     
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa4 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su quinto defensor: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; defensores leyendas")
                print("12; jugador creado")
                d= int(input("ingrese un equipo: "))
                #eso es para eleguir el quinto defensor                
                if d == 1:
                 print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_boca_defensores.keys()))
                 defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 2:
                      print("Posibles defensores: " + ", ".join(formaciones.jugadores_river_defensores.keys()))
                      defensa5 = input("introduzca el nombre de tu quinto  defensor: ")
                elif d == 3:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_racing_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 4:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_independiente_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 5:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_san_lorenzo_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 6:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_rosario_central_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 7:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_argentinos_jr_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 8:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_lanus_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 9:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_belgrano_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 10:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_de_estudiantes_defensores.keys()))
                    defensa5= input("introduzca el nombre de tu quinto defensor: ")
                elif d == 11:
                    print("Posibles defensores: " + ", ".join(formaciones.jugadores_leyenda_defensores.keys()))
                    defensa5 = input("introduzca el nombre de tu quinto defensor: ")
                elif d == 12:
                    print("Posibles defensor: " + ", ", nombrej)
                    defensa5 = input("introduzca el nombre de tu defensor: ")
                clear()
                print("ingrese de que equipo quiere que sea su primer mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyenda")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio1= input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 7:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistaskeys()))
                    medio1 = input("introduzca el nombre de tu primer mediocampista ")  
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio1 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su segundo mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu segundo mediocampista ") 
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio12 = input("introduzca el nombre de tu primer mediocampista ") 
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio12 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su tercero mediocampista: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; mediocampistas leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el tercer mediocampista                
                if m == 1:
                 print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_boca_mediocampistas.keys()))
                 medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 2:
                      print("Posibles mediocampista: " + ", ".join(formaciones.jugadores_de_river_mediocampistas.keys()))
                      medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 3:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_racing_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 4:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_independiente_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 5:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_san_lorenzo_mediocampista.keys()))
                    medio13= input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 6:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_rosario_central_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 7:
                    print("Posibles medocampistas: " + ", ".join(formaciones.jugadores_de_argentinos_jr_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 8:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_lanus_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 9:
                    print("Posibles mediocampistas: " + ", ".join(formaciones.jugadores_de_belgrano_mediocampista.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista: ")
                elif m == 10:
                    print("Posibles mediocampistras: " + ", ".join(formaciones.jugadores_de_estudiantes_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu tercer mediocampista ")  
                elif m == 11:
                    print("Posibles mediocmapista: " + ", ".join(formaciones.jugadores_leyendas_mediocampistas.keys()))
                    medio13 = input("introduzca el nombre de tu primer mediocampista ")    
                elif m == 12:
                    print("Posibles mediocampista: " + ", ", nombrej)
                    medio13 = input("introduzca el nombre de tu mediocampista: ")
                clear()
                print("ingrese de que equipo quiere que sea su primer delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el primer delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero1= input("introduzca el nombre de tu delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero1 = input("introduzca el nombre de tu primer delantero:  ")  
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero1 = input("introduzca el nombre de tu delantero: ") 
                clear()
                print("ingrese de que equipo quiere que sea su segundo delantero: ")
                print("----------------------------------------------------------------")
                print("1; boca")
                print("2; river")
                print("3; racing")
                print("4; independiente")
                print("5; san lorenzo")
                print("6; rosario central")
                print("7; argentinos jr")
                print("8; lanus")
                print("9; belgrano")
                print("10; estudiantes")
                print("11; delanteros leyendas")
                print("12; jugador creado")
                m= int(input("ingrese un equipo: "))
                #eso es para eleguir el segundo delantero               
                if m == 1:
                 print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_boca_delanteros.keys()))
                 delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 2:
                      print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_river_delanteros.keys()))
                      delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 3:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_racing_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 4:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_independiente_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 5:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_san_lorenzo_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 6:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_rosario_central_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 7:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_argentinos_jr_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 8:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_lanus_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero: ")
                elif m == 9:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_belgrano_delantero.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:")
                elif m == 10:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_de_estudiantes_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu segundo delantero:  ")  
                elif m == 11:
                    print("Posibles delantero: " + ", ".join(formaciones.jugadores_leyendas_delanteros.keys()))
                    delantero12 = input("introduzca el nombre de tu primer delantero:  ")   
                elif m == 12:
                    print("Posibles delantero: " + ", ", nombrej)
                    delantero12 = input("introduzca el nombre de tu delantero: ")   
                clear()
                while True:
                    print("Tu equipo final quedó de la siguiente manera:")
                    print()
                    print("Arquero:")
                    print(arquero)
                    print("Defensores:")
                    print(defensa1)
                    print(defensa2)
                    print(defensa3)
                    print(defensa4)
                    print(defensa5)
                    print("Mediocampistas:")
                    print(medio1)
                    print(medio12)
                    print(medio13)
                    print("Delanteros:")
                    print(delantero1)
                    print(delantero12)
                    r = input("Si quieres volver al menú, presiona (1): ")
                    if r == "1":
                        menu()
                        break
                    else:
                        print("Error!")
#diccionario
        if opcion == "2":
            print(                                  )
            print(                                  )
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
            print("11. jugadores leyendas")
            print("12. volver al menu")
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
                        print(formaciones.jugadores_de_boca_delanteros)
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
                            print(formaciones.jugadores_de_estudiantes_mediocampistas)
                            print(                                                                          )
                            print("los delanteros son:  ")
                            print(formaciones.jugadores_de_estudiantes_delanteros)
            elif op == "11":
                print("los jugadores leyendas son: ")
                print(                                                                 )
                print("los arqueros son: ")
                print(formaciones.jugadores_leyendas_arqueros)
                print(                                                    )
                print("los defensores son: ")
                print(formaciones.jugadores_leyenda_defensores)
                print(                                                             )
                print("los mediocampistas son: ")
                print(formaciones.jugadores_leyendas_mediocampistas)
                print(                                                                          )
                print("los delanteros son:  ")
                print(formaciones.jugadores_leyendas_delanteros)
            
            elif op == "12":
                menu()
            while True:
                print(                         )
                print(                             )
                print(                                  )
                e = input("Si quieres volver al menú, presiona (1): ")
                if e == "1":
                    menu()
                    break
                else:
                    print("Error!")


                        
            else: 
                     print('Opcion Invalida, intente otra vez')
        else:
            print("")
menu()