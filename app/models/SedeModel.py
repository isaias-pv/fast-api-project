from database import *
from models.CentroModel import Centro
from typing import Optional
from pydantic import BaseModel, validator

class Sede(Model):
    idSede = AutoField(primary_key=True)
    nombreSede = CharField(max_length=100)
    direccionSede = CharField(max_length=50)
    idCentro = ForeignKeyField(Centro)

    def __str__(self):
        return self.idSede, self.nombreSede, self.direccionSede, self.idCentro

    class Meta:
        database = database

class SedeRequestModel(BaseModel):
    idSede: Optional[int]
    nombreSede: str
    direccionSede: str
    idCentro_id: int

    @validator('nombreSede')
    def nombreSede_length(cls, nombreSede):

        if len(nombreSede) > 100:
            raise ValueError('La longitud máxima es de 100 caracteres.')

        return nombreSede

    @validator('direccionSede')
    def direccionSede_length(cls, direccionSede):

        if len(direccionSede) > 100:
            raise ValueError('La longitud máxima es de 50 caracteres.')

        return direccionSede