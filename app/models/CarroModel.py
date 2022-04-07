from database import *
from models.UsuarioModel import Usuario
from typing import Optional
from pydantic import BaseModel, validator

class Carro(Model):
    idCarro = AutoField(primary_key=True)
    idUsuario = ForeignKeyField(Usuario)
    placa = CharField(max_length=7)

    def __str__(self):
        return self.idCarro, self.idUsuario, self.placa

    class Meta:
        database = database

class CarroRequestModel(BaseModel):
    idCarro: Optional[int]
    idUsuario_id: int
    placa: str