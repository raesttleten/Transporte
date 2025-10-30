from sqlalchemy.orm import Session
import models, schemas

def get_vehiculos(db: Session):
    return db.query(models.Vehiculo).all()

def get_destinos(db: Session):
    return db.query(models.Destino).all()

def create_vehiculo(db: Session, vehiculo: schemas.VehiculoCreate):
    nuevo = models.Vehiculo(**vehiculo.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def create_destino(db: Session, destino: schemas.DestinoCreate):
    nuevo = models.Destino(**destino.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
