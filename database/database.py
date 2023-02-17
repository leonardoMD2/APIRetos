from configs.sqlalchemy_configs import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Retos(Base):
    __tablename__ = 'retos'

    id = Column(Integer, primary_key= True)
    reto = Column(String)
    dificultad = Column(String)
    
class RetosEntregados(Base):
    __tablename__ = 'retos_entregados'

    id = Column(Integer,primary_key=True)
    reto_id = Column(Integer,ForeignKey('retos.id'))
    fecha_entrega =Column(String)