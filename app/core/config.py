from fastapi import FastAPI
from models.models import *
from db.database import database as connection

app = FastAPI(title="ICATIC", description="Backend del Sistema ICA", version="0.1")

@app.on_event('startup')
def startup():#Se ejecuta antes de que el servidor inicie
    if connection.is_closed():
        connection.connect()
        connection.create_tables([Regional,Centro,Sede,Permiso,TipoUsuario,Programa,Ficha,Ambiente,Carro,TipoEquipo,Equipo,Usuario,Bitacora])

@app.on_event('shutdown')
def shutdown():#Se ejecuta cuando el servidor finaliza
    if not connection.is_closed():
        connection.closed()