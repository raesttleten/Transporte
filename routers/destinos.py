from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import get_db

router = APIRouter(prefix="/destinos", tags=["Destinos"])

@router.get("/", response_model=list[schemas.Destino])
def listar_destinos(db: Session = Depends(get_db)):
    return crud.get_destinos(db)

@router.post("/", response_model=schemas.Destino)
def crear_destino(destino: schemas.DestinoCreate, db: Session = Depends(get_db)):
    return crud.create_destino(db, destino)

@router.delete("/{destino_id}")
def eliminar_destino(destino_id: int, db: Session = Depends(get_db)):
    return crud.delete_destino(db, destino_id)
