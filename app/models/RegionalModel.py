from database import *
from typing import Optional
from pydantic import BaseModel, validator

class Regional(Model):
    idRegional = AutoField(primary_key=True)
    codigoRegional = CharField(max_length=10)
    nombreRegional = CharField(max_length=100)

    def __str__(self):
        return self.idRegional, self.codigoRegional, self.nombreRegional

    class Meta:
        database = database

class RegionalRequestModel(BaseModel):
    idRegional: Optional[int]
    codigoRegional: str
    nombreRegional: str

    @validator('codigoRegional')
    def codigoRegional_length(cls, codigoRegional):

        if len(codigoRegional) > 10:
            raise ValueError('La longitud máxima es de 10 caracteres.')

        return codigoRegional

    @validator('nombreRegional')
    def nombreRegional_length(cls, nombreRegional):

        if len(nombreRegional) > 100:
            raise ValueError('La longitud máxima es de 100 caracteres.')

        return nombreRegional