from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Transportes Sigmotoa")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def inicio():
    return {"mensaje": "API Transportes Sigmotoa activa"}

@app.get("/vehiculos/", response_model=list[schemas.Vehiculo])
def listar_vehiculos(db: Session = Depends(get_db)):
    return crud.get_vehiculos(db)

@app.post("/vehiculos/", response_model=schemas.Vehiculo)
def crear_vehiculo(vehiculo: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    return crud.create_vehiculo(db, vehiculo)

@app.get("/destinos/", response_model=list[schemas.Destino])
def listar_destinos(db: Session = Depends(get_db)):
    return crud.get_destinos(db)

@app.post("/destinos/", response_model=schemas.Destino)
def crear_destino(destino: schemas.DestinoCreate, db: Session = Depends(get_db)):
    return crud.create_destino(db, destino)
