from sqlalchemy import Column, Integer, String, Sequence, LargeBinary
from database import connector

class Libro(connector.Manager.Base):
    __tablename__ = 'libros'
    id = Column(Integer, Sequence('libro_id_seq'), primary_key=True)
    titulo = Column(String(50))
    autor = Column(String(50))
    genero = Column(String(15)) #cambiar a genero
    archivo = Column(LargeBinary)
    imagen = Column(LargeBinary)
    nombreimagen = Column(String(200))
    nombrearchivo = Column(String(200))
    rutaarchivo = Column(String(200))
    rutaimagen = Column(String(200))
