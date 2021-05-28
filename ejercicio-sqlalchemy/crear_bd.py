from sqlalchemy import create_engine

engine = create_engine('sqlite:///mundial2k18.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Jugador(Base):
    __tablename__ = 'jugador'

    id = Column(Integer, primary_key=True)
    numJugador = Column(Integer)
    nombreFIFA = Column(String)
    pais = Column(String)
    apellido = Column(String)
    nombres = Column(String)
    dataCamisa = Column(String)
    posicion = Column(String)
    altura = Column(Integer)
    caps = Column(Integer)
    goles = Column(Integer)

    def __repr__(self):
        return "Numero de jugador = %s\nFIFA display = %s\nPais = %s\nApellido = %s\nNombres = %s\nNombre en camisa = %s\nPosicion = %s\nAltura = %d\nCAPS = %d\nGoles = %d\n\n" % (
            self.numJugador, 
            self.nombreFIFA, 
            self.pais,
            self.apellido,
            self.nombres,
            self.dataCamisa,
            self.posicion,
            self.altura,
            self.caps,
            self.goles)

Base.metadata.create_all(engine)
