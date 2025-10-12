""" . """
from pydantic import BaseModel, ConfigDict

class LocalBase(BaseModel):
    """ . """
    nome: str

class LocalCreate(LocalBase):
    """ . """

class LocalResponse(LocalBase):
    """ . """

    class Config:
        model_config = ConfigDict(from_attributes=True)
