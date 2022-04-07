from database import *
from models.UsuarioModel import Usuario
from models.EquipoModel import Equipo
from models.CarroModel import Carro
from models.AmbienteModel import Ambiente
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, validator

class Bitacora(Model):
    idBitacora = AutoField(primary_key=True)
    idUsuario = ForeignKeyField(Usuario)
    idAmbiente = ForeignKeyField(Ambiente)
    idEquipo = ForeignKeyField(Equipo,null=True)
    idCarro = ForeignKeyField(Carro,null=True)
    fechaHoraIngreso = DateTimeField()
    fechaHoraSalida = DateTimeField(null=True)

    def __str__(self):
        return self.idBitacora, self.idUsuario, self.idAmbiente,self.idEquipo, self.idCarro, self.fechaHoraIngreso, self.fechaHoraSalida

    class Meta:
        database = database

class BitacoraRequestModel(BaseModel):
    idBitacora: Optional[int]
    idUsuario_id: int
    idAmbiente_id: int
    idEquipo_id: Optional[int]
    idCarro_id: Optional[int]
    fechaHoraIngreso: datetime
    fechaHoraSalida: Optional[datetime]