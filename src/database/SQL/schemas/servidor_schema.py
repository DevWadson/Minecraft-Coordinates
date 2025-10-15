""" . """
from pydantic import BaseModel, ConfigDict

class ServidorBase(BaseModel):
    """ . """
    nome: str

class ServidorCreate(ServidorBase):
    """ . """
    pass

class ServidorResponse(ServidorBase):
    """ . """
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)
