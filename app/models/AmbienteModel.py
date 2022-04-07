from database import *
from models.models import Sede
from typing import Optional
from pydantic import BaseModel, validator

class Ambiente(Model):
    idAmbiente = AutoField(primary_key=True)
    pisoAmbiente = CharField(max_length=2)
    nombreAmbiente = CharField(max_length=20)
    idSede = ForeignKeyField(Sede)

    def __str__(self):
        return self.idAmbiente, self.pisoAmbiente, self.nombreAmbiente, self.idSede

    class Meta:
        database = database

class AmbienteRequestModel(BaseModel):
    idAmbiente: Optional[int]
    pisoAmbiente: str
    nombreAmbiente: str
    idSede_id: int