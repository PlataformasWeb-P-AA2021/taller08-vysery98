# Presentar todos los jugadores ordenados por el número de goles

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_bd import Jugador

engine = create_engine('sqlite:///mundial2k18.db')

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Jugador).order_by(Jugador.goles).all()
print(query)