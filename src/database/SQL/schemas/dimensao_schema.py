""" . """
from pydantic import BaseModel, ConfigDict

class DimensaoBase(BaseModel):
    """ . """
    nome: str

class DimensaoCreate(DimensaoBase):
    """ . """

class DimensaoResponse(DimensaoBase):
    """ . """
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)
