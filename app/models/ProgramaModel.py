from database import *
from typing import Optional
from pydantic import BaseModel, validator

class Programa(Model):
    idPrograma = AutoField(primary_key=True)
    nombrePrograma = CharField(max_length=200)

    def __str__(self):
        return self.idPrograma, self.nombrePrograma

    class Meta:
        database = database

class ProgramaRequestModel(BaseModel):
    idPrograma: Optional[int]
    nombrePrograma: str