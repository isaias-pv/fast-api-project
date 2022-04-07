from config import *
from models.RegionalModel import RegionalRequestModel

@app.post('/regional')

async def create_regional(regionalRequest: RegionalRequestModel):
    regional = Regional.create(
        codigoRegional=regionalRequest.codigoRegional,
        nombreRegional=regionalRequest.nombreRegional
    )
    return "Regional Creada"