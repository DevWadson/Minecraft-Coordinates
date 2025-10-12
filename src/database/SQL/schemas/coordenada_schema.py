""" . """
from pydantic import BaseModel, ConfigDict

class CoordenadaBase(BaseModel):
    """ . """
    x: float
    y: float
    z: float

class CoordenadaCreate(CoordenadaBase):
    """ . """

class CooredenadaResponse(CoordenadaBase):
    """ . """

    class Config:
        model_config = ConfigDict(from_attributes=True)
