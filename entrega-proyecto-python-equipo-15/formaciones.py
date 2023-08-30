class JUGADOR:
    def __init__ (self, edad:int, estado_fisico:str, posicion:str, nacionalidad:str, valor_de_mercado:int, ):
        self.edad = edad
        self.estado_fisico = estado_fisico
        self.posicion = posicion
        self.nacionalidad = nacionalidad
        self.valor_de_mercado = valor_de_mercado


jugadores_de_boca = {"sergio romero": {"Edad": 35, "Posición": "Portero", "Valor de Mercado": 15000000, "Valoración": 8}, 
"leandro brey": {"Edad": 20, "Posición": "Portero", "Valor de Mercado": 6000000, "Valoración": 7},
}
jugadores_de_boca_defensores = {
                "marcelo weigandt": {"Edad": 27, "Posición": "Defensor", "Valor de Mercado": 7000000, "Valoración": 9},
                "nicolas valentini": {"Edad": 21, "Posición": "Defensor", "Valor de Mercado": 3000000, "Valoración": 8},
                "nicolas figal": {"Edad": 29, "Posición": "Defensor", "Valor de Mercado": 9000000, "Valoración": 7},
                "frank fabra": {"Edad": 33, "Posición": "Defensor", "Valor de Mercado": 7000000, "Valoración": 9},
                "luis advíncula": {"Edad": 28, "Posición": "Defensor", "Valor de Mercado": 12000000, "Valoración": 9},
            }
jugadores_de_boca_mediocampistas ={
                "pol fernandez": {"Edad": 31, "Posición": "Volante", "Valor de Mercado": 9000000, "Valoración": 8},
                "alan varela": {"Edad": 24, "Posición": "Volante", "Valor de Mercado": 9000000, "Valoración": 8},
                "juan ramirez": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 5000000, "Valoración": 8},
                "cristian medina": {"Edad": 22, "Posición": "Volante", "Valor de Mercado": 9000000, "Valoración": 9},
            }
jugadores_de_boca_delanteros ={
                "edinson cavani": {"Edad": 31, "Posición": "Volante", "Valor de Mercado": 9000000, "Valoración": 8},
                "dario benedetto": {"Edad": 24, "Posición": "Volante", "Valor de Mercado": 9000000, "Valoración": 8},
                "miguel merentiel": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 5000000, "Valoración": 8},
            }

jugadores_river = {
    "franco armani": {"Edad": 34, "Posición": "Portero", "Valor de Mercado": 10000000, "Valoración": 9},
    "germán lux": {"Edad": 39, "Posición": "Portero", "Valor de Mercado": 1500000, "Valoración": 6},
}
jugadores_river_defensores = {
    "gonzalo montiel": {"Edad": 25, "Posición": "Defensor", "Valor de Mercado": 20000000, "Valoración": 8},
    "hector martinez": {"Edad": 25, "Posición": "Defensor", "Valor de Mercado": 7000000, "Valoración": 7},
    "david martinez": {"Edad": 24, "Posición": "Defensor", "Valor de Mercado": 8000000, "Valoración": 7},
    "jonatan maidana": {"Edad": 36, "Posición": "Defensor", "Valor de Mercado": 5000000, "Valoración": 8},
    "milton casco": {"Edad": 33, "Posición": "Defensor", "Valor de Mercado": 9000000, "Valoración": 8},
}
jugadores_de_river_mediocampistas = {
    "enzo perez": {"Edad": 35, "Posición": "Volante", "Valor de Mercado": 12000000, "Valoración": 9},
    "nicolas de la cruz": {"Edad": 24, "Posición": "Volante", "Valor de Mercado": 15000000, "Valoración": 8},
    "enzo fernandez": {"Edad": 21, "Posición": "Volante", "Valor de Mercado": 10000000, "Valoración": 7},
    "bruno zuculini": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 7000000, "Valoración": 7},
}
jugadores_de_river_delanteros ={
     "julian alvarez": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 20000000, "Valoración": 9},
    "matias suarez": {"Edad": 34, "Posición": "Delantero", "Valor de Mercado": 12000000, "Valoración": 8},
    "rafael borre": {"Edad": 25, "Posición": "Delantero", "Valor de Mercado": 18000000, "Valoración": 9},
    "jorge carrascal": {"Edad": 23, "Posición": "Delantero", "Valor de Mercado": 10000000, "Valoración": 7}


}

jugadores_racing= {
    "gabriel arias": {"Edad": 34, "Posición": "Portero", "Valor de Mercado": 8000000, "Valoración": 8},
    "juan jose Caceres": {"Edad": 22, "Posición": "Portero", "Valor de Mercado": 3000000, "Valoración": 7},
}
jugadores_racing_defensores ={
    "leonardo sigali": {"Edad": 34, "Posición": "Defensor", "Valor de Mercado": 5000000, "Valoración": 8},
    "nery dominguez": {"Edad": 31, "Posición": "Defensor", "Valor de Mercado": 4000000, "Valoración": 7},
    "eugenio mena": {"Edad": 33, "Posición": "Defensor", "Valor de Mercado": 6000000, "Valoración": 8},
    "joquin novillo": {"Edad": 24, "Posición": "Defensor", "Valor de Mercado": 2000000, "Valoración": 7},
    "juan jose caceres": {"Edad": 21, "Posición": "Defensor", "Valor de Mercado": 3000000, "Valoración": 7},
}
jugadores_racing_mediocampistas = {
    "leonel miranda": {"Edad": 29, "Posición": "Volante", "Valor de Mercado": 6000000, "Valoración": 7},
    "matias rojas": {"Edad": 25, "Posición": "Volante", "Valor de Mercado": 9000000, "Valoración": 8},
    "ignacio piatti": {"Edad": 36, "Posición": "Volante", "Valor de Mercado": 7000000, "Valoración": 8},
}
jugadores_de_racing_delanteros = {
    "anibal moreno": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 3000000, "Valoración": 7},
    "tomas chancalay": {"Edad": 23, "Posición": "Delantero", "Valor de Mercado": 8000000, "Valoración": 7},
    "dario cvitanich": {"Edad": 37, "Posición": "Delantero", "Valor de Mercado": 4000000, "Valoración": 7},
    "nicolas reniero": {"Edad": 26, "Posición": "Delantero", "Valor de Mercado": 6000000, "Valoración": 8}
}

jugadores_independiente = {
    "sebastian sosa": {"Edad": 35, "Posición": "Portero", "Valor de Mercado": 5000000, "Valoración": 8},
    "milton alvarez": {"Edad": 33, "Posición": "Portero", "Valor de Mercado": 2000000, "Valoración": 7},
}
jugadores_de_independiente_defensores ={
    "alan franco": {"Edad": 24, "Posición": "Defensor", "Valor de Mercado": 10000000, "Valoración": 8},
    "juan manuel insaurralde": {"Edad": 37, "Posición": "Defensor", "Valor de Mercado": 4000000, "Valoración": 7},
    "sergio barreto": {"Edad": 21, "Posición": "Defensor", "Valor de Mercado": 6000000, "Valoración": 7},
    "fabricio bustos": {"Edad": 25, "Posición": "Defensor", "Valor de Mercado": 8000000, "Valoración": 8},
    "lucas rodriguez": {"Edad": 24, "Posición": "Defensor", "Valor de Mercado": 7000000, "Valoración": 8},
    "ayrton costa": {"Edad": 23, "Posición": "Defensor", "Valor de Mercado": 3000000, "Valoración": 7},
}    
jugadores_de_independiente_mediocampistas = {
    "alan velasco": {"Edad": 19, "Posición": "Volante", "Valor de Mercado": 12000000, "Valoración": 9},
    "lucas romero": {"Edad": 27, "Posición": "Volante", "Valor de Mercado": 9000000, "Valoración": 8},
    "domingo blanco": {"Edad": 27, "Posición": "Volante", "Valor de Mercado": 6000000, "Valoración": 7},
    "andres roa": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 7000000, "Valoración": 7},
}
jugadores_de_independiente_delanteros ={
    "silvio romero": {"Edad": 34, "Posición": "Delantero", "Valor de Mercado": 8000000, "Valoración": 9},
    "jonathan menendez": {"Edad": 25, "Posición": "Delantero", "Valor de Mercado": 5000000, "Valoración": 7},
    "braian martinez": {"Edad": 24, "Posición": "Delantero", "Valor de Mercado": 6000000, "Valoración": 8},
    "juan insaurralde": {"Edad": 36, "Posición": "Delantero", "Valor de Mercado": 3000000, "Valoración": 7}
}

jugadores_san_lorenzo = {
    "sebastian torrico": {"Edad": 42, "Posición": "Portero", "Valor de Mercado": 1000000, "Valoración": 7},
    "jose devecchi": {"Edad": 25, "Posición": "Portero", "Valor de Mercado": 2000000, "Valoración": 7},
}
jugadores_de_san_lorenzo_defensores = {
    "gonzalo rodriguez": {"Edad": 37, "Posición": "Defensor", "Valor de Mercado": 3000000, "Valoración": 8},
    "fabian licha": {"Edad": 22, "Posición": "Defensor", "Valor de Mercado": 2000000, "Valoración": 6},
    "gino peruzzi": {"Edad": 29, "Posición": "Defensor", "Valor de Mercado": 4000000, "Valoración": 7},
    "diego braghieri": {"Edad": 35, "Posición": "Defensor", "Valor de Mercado": 2500000, "Valoración": 7},
    "bruno pitton": {"Edad": 27, "Posición": "Defensor", "Valor de Mercado": 3500000, "Valoración": 7},
}
jugadores_de_san_lorenzo_mediocampista = {
    "juan ramirez": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 5000000, "Valoración": 8},
    "oscar romero": {"Edad": 29, "Posición": "Volante", "Valor de Mercado": 8000000, "Valoración": 9},
    "angel romero": {"Edad": 30, "Posición": "Volante", "Valor de Mercado": 8000000, "Valoración": 8},
    "nahuel barrios": {"Edad": 24, "Posición": "Volante", "Valor de Mercado": 3000000, "Valoración": 7},
}
jugadores_de_san_lorenzo_delantero = {
    "alex diaz": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 4000000, "Valoración": 7},
    "Fernando monetti": {"Edad": 32, "Posición": "Delantero", "Valor de Mercado": 2000000, "Valoración": 7},
    "adolfo gaich": {"Edad": 22, "Posición": "Delantero", "Valor de Mercado": 6000000, "Valoración": 8},
    "franco di santo": {"Edad": 32, "Posición": "Delantero", "Valor de Mercado": 3500000, "Valoración": 7}
}


jugadores_rosario_central= {
    "jeremias ledesma": {"Edad": 28, "Posición": "Portero", "Valor de Mercado": 2500000, "Valoración": 7},
    "mauricio caranta": {"Edad": 42, "Posición": "Portero", "Valor de Mercado": 500000, "Valoración": 6},
}
jugadores_de_rosario_central_defensores = {
    "damian martinez": {"Edad": 28, "Posición": "Defensor", "Valor de Mercado": 5000000, "Valoración": 8},
    "jonathan bottinelli": {"Edad": 37, "Posición": "Defensor", "Valor de Mercado": 2000000, "Valoración": 7},
    "nahuel molina": {"Edad": 24, "Posición": "Defensor", "Valor de Mercado": 6000000, "Valoración": 8},
    "joel lopez pissano": {"Edad": 26, "Posición": "Defensor", "Valor de Mercado": 1500000, "Valoración": 6},
}
jugadores_de_rosario_central_mediocampistas = {
    "emmanuel ojeda": {"Edad": 22, "Posición": "Volante", "Valor de Mercado": 3500000, "Valoración": 7},
    "diego zabala": {"Edad": 26, "Posición": "Volante", "Valor de Mercado": 3000000, "Valoración": 6},
    "fabian rinaudo": {"Edad": 34, "Posición": "Volante", "Valor de Mercado": 2000000, "Valoración": 7},
    "luciano ferreyra": {"Edad": 23, "Posición": "Volante", "Valor de Mercado": 2000000, "Valoración": 6},
}
jugadores_de_rosario_central_delanteros = {
    "marco ruben": {"Edad": 34, "Posición": "Delantero", "Valor de Mercado": 5000000, "Valoración": 8},
    "lucas gamba": {"Edad": 32, "Posición": "Delantero", "Valor de Mercado": 4000000, "Valoración": 7},
    "joao rodriguez": {"Edad": 25, "Posición": "Delantero", "Valor de Mercado": 3000000, "Valoración": 7},
    "luciano cingolani": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 2000000, "Valoración": 6},
    "alejo veliz": {"Edad": 24, "Posición": "Delantero", "Valor de Mercado": 2500000, "Valoración": 7},
    "mateo bounanotte": {"Edad": 25, "Posición": "Delantero", "Valor de Mercado": 3000000, "Valoración": 7}
}


jugadores_argentinos_junior = {
    "lucas chaves": {"Edad": 26, "Posición": "Portero", "Valor de Mercado": 2000000, "Valoración": 7},
    "federico lanzillotta": {"Edad": 32, "Posición": "Portero", "Valor de Mercado": 800000, "Valoración": 6},
}
jugadores_de_argentinos_jr_defensores= {
    "carlos quintana": {"Edad": 33, "Posición": "Defensor", "Valor de Mercado": 3000000, "Valoración": 7},
    "miguel torren": {"Edad": 34, "Posición": "Defensor", "Valor de Mercado": 2500000, "Valoración": 7},
    "jonathan sandoval": {"Edad": 29, "Posición": "Defensor", "Valor de Mercado": 1500000, "Valoración": 6},
    "elias gomez": {"Edad": 23, "Posición": "Defensor", "Valor de Mercado": 4000000, "Valoración": 8},
}
jugadores_de_argentinos_jr_mediocampistas = {
    "gabriel florentin": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 2500000, "Valoración": 7},
    "franco moyano": {"Edad": 25, "Posición": "Volante", "Valor de Mercado": 1800000, "Valoración": 6},
    "gabriel carabajal": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 3500000, "Valoración": 7},
    "matias romero": {"Edad": 22, "Posición": "Volante", "Valor de Mercado": 3000000, "Valoración": 7},
    "nicolas silva": {"Edad": 27, "Posición": "volante", "Valor de Mercado": 2000000, "Valoración": 7}

}
jugadores_de_argentinos_jr_delantero = {
    "gabriel avalos": {"Edad": 28, "Posición": "Delantero", "Valor de Mercado": 4000000, "Valoración": 7},
    "lucas ambrogio": {"Edad": 23, "Posición": "Delantero", "Valor de Mercado": 2000000, "Valoración": 6},
    "gabriel hauche": {"Edad": 34, "Posición": "Delantero", "Valor de Mercado": 1800000, "Valoración": 7},
    "mateo coronel": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 1500000, "Valoración": 6},
    "nicolas silva": {"Edad": 27, "Posición": "Defensor", "Valor de Mercado": 2000000, "Valoración": 7}
}


jugadores_lanus = {
    "lautaro morales": {"Edad": 22, "Posición": "Portero", "Valor de Mercado": 1500000, "Valoración": 7},
    "lucas acosta": {"Edad": 26, "Posición": "Portero", "Valor de Mercado": 800000, "Valoración": 6},
}
jugadores_de_lanus_defensores = {
    "nicolas morgantini": {"Edad": 27, "Posición": "Defensor", "Valor de Mercado": 900000, "Valoración": 7},
    "alexis perez": {"Edad": 28, "Posición": "Defensor", "Valor de Mercado": 1200000, "Valoración": 7},
    "ezequiel muñoz": {"Edad": 31, "Posición": "Defensor", "Valor de Mercado": 1000000, "Valoración": 6},
    "brian aguirre": {"Edad": 23, "Posición": "Defensor", "Valor de Mercado": 800000, "Valoración": 6},
}
jugadores_de_lanus_mediocampistas = {
    "tomas belmonte": {"Edad": 23, "Posición": "Volante", "Valor de Mercado": 2000000, "Valoración": 8},
    "facundo perez": {"Edad": 20, "Posición": "Volante", "Valor de Mercado": 1500000, "Valoración": 7},
    "alexis perez": {"Edad": 26, "Posición": "Volante", "Valor de Mercado": 1200000, "Valoración": 7},
    "pedro de la vega": {"Edad": 20, "Posición": "Volante", "Valor de Mercado": 2000000, "Valoración": 8},
    "ignacio cechi": {"Edad": 22, "Posición": "Volante", "Valor de Mercado": 600000, "Valoración": 6},
}
jugadores_de_lanus_delanteros = {
    "jose sand": {"Edad": 41, "Posición": "Delantero", "Valor de Mercado": 800000, "Valoración": 7},
    "nicolas orsini": {"Edad": 26, "Posición": "Delantero", "Valor de Mercado": 1800000, "Valoración": 7},
    "franco orozco": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 1000000, "Valoración": 6},
    "matias esquivel": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 900000, "Valoración": 6},
}



jugadores_belgrano = {
    "nahuel losada": {"Edad": 23, "Posición": "Portero", "Valor de Mercado": 800000, "Valoración": 9},
}
jugadores_de_belgrano_defensores = {
    "juan barinaga": {"Edad": 22, "Posición": "Defensor", "Valor de Mercado": 600000, "Valoración": 8},
    "nicolas meriano": {"Edad": 24, "Posición": "Defensor", "Valor de Mercado": 700000, "Valoración": 9},
    "matias moreno": {"Edad": 25, "Posición": "Defensor", "Valor de Mercado": 900000, "Valoración": 8},
    "alejandro rebola": {"Edad": 26, "Posición": "Defensor", "Valor de Mercado": 800000, "Valoración": 8},
    "alex ibacache": {"Edad": 20, "Posición": "Defensor", "Valor de Mercado": 500000, "Valoración": 7},
}
jugadores_de_belgrano_mediocampista = {
    "matias marin": {"Edad": 34, "Posición": "Volante", "Valor de Mercado": 800000, "Valoración": 8},
    "santiago longo": {"Edad": 35, "Posición": "Volante", "Valor de Mercado": 600000, "Valoración": 10},
    "bruno zapelli": {"Edad": 23, "Posición": "Volante", "Valor de Mercado": 700000, "Valoración": 10},
    "ulises sanchez": {"Edad": 22, "Posición": "Volante", "Valor de Mercado": 500000, "Valoración": 10},
    "chino castro": {"Edad": 25, "Posición": "Volante", "Valor de Mercado": 800000, "Valoración": 9},
}
jugadores_de_belgrano_delantero = {
    "lautaro pastran": {"Edad": 23, "Posición": "Delantero", "Valor de Mercado": 700000, "Valoración": 9},
    "daniel barrea": {"Edad": 23, "Posición": "Delantero", "Valor de Mercado": 600000, "Valoración": 10},
    "pablo vegetti": {"Edad": 20, "Posición": "Delantero", "Valor de Mercado": 800000, "Valoración": 10},
    "ibrahim hesar": {"Edad": 32, "Posición": "Delantero", "Valor de Mercado": 900000, "Valoración": 8}
}


jugadores_estudiantes= {
    "mariano andujar": {"Edad": 37, "Posición": "Portero", "Valor de Mercado": 2000000, "Valoración": 8},
    "emiliano gonzalez": {"Edad": 23, "Posición": "Portero", "Valor de Mercado": 800000, "Valoración": 6},
}
jugadores_de_estudiantes_defensores = {
    "fabian noguera": {"Edad": 29, "Posición": "Defensor", "Valor de Mercado": 1500000, "Valoración": 7},
    "nazareno colombo": {"Edad": 21, "Posición": "Defensor", "Valor de Mercado": 1000000, "Valoración": 7},
    "agustin rogel": {"Edad": 23, "Posición": "Defensor", "Valor de Mercado": 1200000, "Valoración": 7},
    "facundo mura": {"Edad": 22, "Posición": "Defensor", "Valor de Mercado": 1000000, "Valoración": 7},
}
jugadores_de_estudiantes_mediocampistas = {
    "sanchez miño": {"Edad": 32, "Posición": "Volante", "Valor de Mercado": 1800000, "Valoración": 8},
    "nicolas pasquini": {"Edad": 28, "Posición": "Volante", "Valor de Mercado": 1500000, "Valoración": 7},
    "ivan gomez": {"Edad": 23, "Posición": "Volante", "Valor de Mercado": 1000000, "Valoración": 7},
    "julian marchioni": {"Edad": 21, "Posición": "Volante", "Valor de Mercado": 800000, "Valoración": 6},
}
jugadores_de_estudiantes_delanteros={
    "federico gonzalez": {"Edad": 26, "Posición": "Delantero", "Valor de Mercado": 2000000, "Valoración": 8},
    "rodrigo bogado": {"Edad": 21, "Posición": "Delantero", "Valor de Mercado": 1200000, "Valoración": 7},
    "martin cauteruccio": {"Edad": 34, "Posición": "Delantero", "Valor de Mercado": 1500000, "Valoración": 7},
    "juan apaolaza": {"Edad": 23, "Posición": "Delantero", "Valor de Mercado": 800000, "Valoración": 7},
    "juan noelia": {"Edad": 23, "Posición": "Volante", "Valor de Mercado": 700000, "Valoración": 7},
}
jugadores_leyendas_arqueros={
    "gianluigi buffon": { "edad": 20, "posicion": "defenspr", "valor de mercado": 120000000, "valoracion": 10},
    "iker casillas":{"edad": 20, "posicion":"defensor", "valor de mercado": 140000000, "valoracion": 10},
    "nery pumpido":{"edad": 27, "posicion": "defensor", "valor de mercado": 180000000, "valoracion": 10},
    "manuel neuer":{"edad": 25, "posicion": "defensor", "valor de mercado": 120000000, "valoracion": 10},

}
jugadores_leyenda_defensores={
    "paolo maldini": { "edad": 25, "posicion": "defenspr", "valor de mercado": 130000000, "valoracion": 10},
    "fabio cannavaro":{"edad": 27, "posicion":"defensor", "valor de mercado": 120000000, "valoracion": 10},
    "sergio ramos":{"edad": 25, "posicion": "defensor", "valor de mercado": 110000000, "valoracion": 10},
    "Franz Beckenbauer":{"edad": 27, "posicion": "defensor", "valor de mercado": 170000000, "valoracion": 10},

}
jugadores_leyendas_mediocampistas={
    "zinedin zidane": { "edad": 25, "posicion": "mediocampista", "valor de mercado": 125000000, "valoracion": 10},
    "fernando redondo":{"edad": 27, "posicion":"mediocampista", "valor de mercado": 125000000, "valoracion": 10},
    "patrick vieira":{"edad": 25, "posicion": "mediocampista", "valor de mercado": 150000000, "valoracion": 10},
    "andrea pirlo":{"edad": 25, "posicion": "mediocampista", "valor de mercado": 130000000, "valoracion": 10},

}

jugadores_leyendas_delanteros={
    "diego maradona":{"Edad":25,"Posición":"Delantero", "Valor de Mercado": 125000000,"Valoración":10},
    "pele":{"Edad":29,"Posición":"Delantero", "Valor de Mercado": 150000000,"Valoración":10},
    "johan cruyff":{"Edad":27,"Posición":"Delantero", "Valor de Mercado": 150000000,"Valoración":10},
    "lionel messi":{"Edad":25,"Posición":"Delantero", "Valor de Mercado": 125000000,"Valoración":10},
    "neymar jr":{"Edad":22,"Posición":"Delantero", "Valor de Mercado": 100000000,"Valoración":10},
    "cristiano ronaldo":{"Edad":29,"Posición":"Delantero", "Valor de Mercado": 122000000,"Valoración":10},




}
