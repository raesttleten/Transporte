from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import get_db

router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])

@router.get("/", response_model=list[schemas.Vehiculo])
def listar_vehiculos(db: Session = Depends(get_db)):
    return crud.get_vehiculos(db)

@router.post("/", response_model=schemas.Vehiculo)
def crear_vehiculo(vehiculo: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    return crud.create_vehiculo(db, vehiculo)

@router.delete("/{vehiculo_id}")
def eliminar_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    return crud.delete_vehiculo(db, vehiculo_id)
