from sqlalchemy import Column, Integer, String, Sequence, LargeBinary,Boolean
from database import connector

class mobileUser(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255, collation='NOCASE'), nullable=False, unique=True)
    password = Column(String(255), nullable=False, server_default='')

class Libro(connector.Manager.Base):
    __tablename__ = 'libros'
    ID = Column(Integer, Sequence('libro_id_seq'), primary_key=True)
    titulo = Column(String(50))
    autor = Column(String(50))
    nacionalidad = Column(String(60))
    genero = Column(String(15))
    descripcion= Column(String(500))
    archivo = Column(LargeBinary)
    imagen = Column(LargeBinary)
    fotoautor=Column(LargeBinary)
    nombreimagen = Column(String(200))
    nombrearchivo = Column(String(200))
    nombrefotoautor=Column(String(200))
    rutaarchivo = Column(String(200))
    rutaimagen = Column(String(200))
    rutafotoautor= Column(String(200))
    # Favorite=Column(Boolean)
