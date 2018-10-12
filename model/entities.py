from sqlalchemy import Column, Integer, String, Sequence, LargeBinary
from database import connector

class Libro(connector.Manager.Base):
    __tablename__ = 'libros'
    id = Column(Integer, Sequence('libro_id_seq'), primary_key=True)
    titulo = Column(String(50))
    autor = Column(String(50))
    tipo = Column(String(15))
    imagen = Column(LargeBinary)
    archivo = Column(LargeBinary)
