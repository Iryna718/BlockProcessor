from pydantic import BaseModel, Field
from typing import Optional

class Person(BaseModel):
    id: int = Field(gt=200)
    name: str = Field(min_length=2)
    addr: str = Field(min_length=5)

class Source(BaseModel):
    id: int = Field(gt=0)
    ip_addr: str = Field(pattern=r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    country_code: str = Field(pattern=r"^[A-Z]{2}$")

class Block(BaseModel):
    id: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
    view: int = Field(ge=0)
    desc: str
    img: Optional[bytes] = None

class Vote(BaseModel):
    block_id: str = Field(pattern=r"^[0-9a-fA-F]{8}$")
    voter_id: int = Field(gt=0)
    timestamp: str
    source_id: int = Field(gt=0)
