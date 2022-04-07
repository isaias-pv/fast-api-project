from database import *
from typing import Optional
from pydantic import BaseModel, validator

class Permiso(Model):
    idPermiso= AutoField(primary_key=True)
    nombrePermiso = CharField(max_length=200)

    def __str__(self):
        return self.idPermiso, self.nombrePermiso

    class Meta:
        database = database

class PermisoRequestModel(BaseModel):
    idPermiso: Optional[int]
    nombrePermiso: str