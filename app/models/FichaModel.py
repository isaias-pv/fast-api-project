from database import *
from models.ProgramaModel import Programa
from typing import Optional
from pydantic import BaseModel, validator

class Ficha(Model):
    idFicha = AutoField(primary_key=True)
    numeroFicha = CharField(max_length=20)
    nombreFicha = CharField(max_length=20)
    idPrograma = ForeignKeyField(Programa)

    def __str__(self):
        return self.idFicha, self.numeroFicha, self.nombreFicha, self.idPrograma

    class Meta:
        database = database

class FichaRequestModel(BaseModel):
    idFicha: Optional[int]
    numeroFicha: str
    nombreFicha: str
    idPrograma_id: int