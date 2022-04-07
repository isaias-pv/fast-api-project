from database import *
from models.SedeModel import Sede
from models.TipoUsuarioModel import TipoUsuario
from models.FichaModel import Ficha
from typing import Optional
from pydantic import BaseModel, validator, EmailStr

class Usuario(Model):
    idUsuario = AutoField(primary_key=True)
    idTipoUsuario = ForeignKeyField(TipoUsuario)
    idSede = ForeignKeyField(Sede,null=True)
    idFicha = ForeignKeyField(Ficha,null=True)
    tipoIdentificacion = CharField(max_length=4)
    numeroIdentificacion = CharField(max_length=30)
    nombres = CharField(max_length=200)
    apellidos = CharField(max_length=200)
    password= CharField(max_length=20)
    email = CharField(max_length=50)
    token = CharField(max_length=30)

    def __str__(self):
        return self.idUsuario, self.idTipoUsuario, self.idSede, self.idFicha, self.tipoIdentificacion, self.numeroIdentificacion,self.nombres, self.apellidos, self.password, self.email, self.token

    class Meta:
        database = database

class UsuarioRequestModel(BaseModel):
    idUsuario: Optional[int]
    idTipoUsuario_id: int
    idSede_id: Optional[int]
    idFicha_id: Optional[int]
    tipoIdentificacion: str
    numeroIdentificacion: str
    nombres: str
    apellidos: str
    password: str
    email: EmailStr
    token: str