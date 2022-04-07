from database import *
from models.RegionalModel import Regional
from typing import Optional
from pydantic import BaseModel, validator

class Centro(Model):
    idCentro = AutoField(primary_key=True)
    codigoCentro = CharField(max_length=10)
    nombreCentro = CharField(max_length=100)
    idRegional = ForeignKeyField(Regional)

    def __str__(self):
        return self.idCentro, self.codigoCentro, self.nombreCentro, self.idRegional

    class Meta:
        database = database

class CentroRequestModel(BaseModel):
    idCentro: Optional[int]
    codigoCentro: str
    nombreCentro: str
    idRegional_id: int

    @validator('codigoCentro')
    def codigoCentro_length(cls, codigoCentro):

        if len(codigoCentro) > 10:
            raise ValueError('La longitud máxima es de 10 caracteres.')

        return codigoCentro

    @validator('nombreCentro')
    def nombreCentro_length(cls, nombreCentro):

        if len(nombreCentro) > 100:
            raise ValueError('La longitud máxima es de 100 caracteres.')

        return nombreCentro