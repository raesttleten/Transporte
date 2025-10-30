from pydantic import BaseModel
from typing import List, Optional

class DestinoBase(BaseModel):
    ciudad_destino: str
    distancia_km: float
    valor_pasaje: float
    id_vehiculo: int

class DestinoCreate(DestinoBase):
    pass

class Destino(DestinoBase):
    id: int
    class Config:
        orm_mode = True


class VehiculoBase(BaseModel):
    placa: str
    marca: str
    modelo: str
    capacidad: int

class VehiculoCreate(VehiculoBase):
    pass

class Vehiculo(VehiculoBase):
    id: int
    destinos: List[Destino] = []
    class Config:
        orm_mode = True
