from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_bd import Jugador

import csv

engine = create_engine('sqlite:///mundial2k18.db')

Session = sessionmaker(bind=engine)
session = Session()

with open('data/mundial2018.csv') as file:
    data = csv.reader(file, delimiter = '|')
    # Salto de encabezado
    next(data)

    for i in data:
        # Prueba de salida -> print(i)
        # Prueba de salida -> print(i[1])
        player = Jugador(numJugador = i[0], nombreFIFA = i[1], pais = i[2],
                    apellido = i[3], nombres = i[4], dataCamisa = i[5],
                    posicion = i[6], altura = i[7], caps = i[8], goles = i[9])
        # Agregar Data
        session.add(player)

# Confirmar transacciones
session.commit()