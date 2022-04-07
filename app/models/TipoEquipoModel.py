from database import *
from typing import Optional
from pydantic import BaseModel, validator

class TipoEquipo(Model):
    idTipoEquipo = AutoField(primary_key=True)
    nombreEquipo = CharField(max_length=200)

    def __str__(self):
        return self.idTipoEquipo, self.nombreEquipo

    class Meta:
        database = database

class TipoEquipoRequestModel(BaseModel):
    idTipoEquipo: Optional[int]
    nombreTipoEquipo: str