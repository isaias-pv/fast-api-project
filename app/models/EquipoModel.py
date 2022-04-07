from database import *
from models.TipoEquipoModel import TipoEquipo
from models.UsuarioModel import Usuario
from typing import Optional
from pydantic import BaseModel, validator

class Equipo(Model):
    idEquipo = AutoField(primary_key=True)
    idUsuario = ForeignKeyField(Usuario)
    idTipoEquipo = ForeignKeyField(TipoEquipo)
    serial = CharField(max_length=50)
    marca = CharField(max_length=50)

    def __str__(self):
        return self.idEquipo, self.idUsuario, self.idTipoEquipo, self.serial, self.marca

    class Meta:
        database = database

class EquipoRequestModel(BaseModel):
    idEquipo: Optional[int]
    idUsuario_id: int
    idTipoEquipo_id: int
    serial: str
    marca: str