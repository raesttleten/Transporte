from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    capacidad = Column(Integer)

    destinos = relationship("Destino", back_populates="vehiculo")

class Destino(Base):
    __tablename__ = "destinos"

    id = Column(Integer, primary_key=True, index=True)
    ciudad_destino = Column(String)
    distancia_km = Column(Float)
    valor_pasaje = Column(Float)
    id_vehiculo = Column(Integer, ForeignKey("vehiculos.id"))

    vehiculo = relationship("Vehiculo", back_populates="destinos")
