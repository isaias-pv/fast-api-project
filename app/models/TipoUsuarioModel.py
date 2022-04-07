from database import *
from typing import Optional
from pydantic import BaseModel, validator

class TipoUsuario(Model):
    idTipoUsuario = AutoField(primary_key=True)
    nombreTipoUsuario = CharField(max_length=100)
    permisos = CharField(max_length=50)

    def __str__(self):
        return self.idTipoUsuario, self.nombreTipoUsuario, self.permisos

    class Meta:
        database = database

class TipoUsuarioRequestModel(BaseModel):
    idTipoUsuario: Optional[int]
    nombreTipoUsuario: str
    permiso: list