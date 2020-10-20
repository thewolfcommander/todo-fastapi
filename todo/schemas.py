from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    """
    This is common model for request and response
    """
    title: str
    description: Optional[str] = None
    status: Optional[str] = 'ongoing'


class TodoCreate(TodoBase):
    """
    This is model for requests or creating todos
    """
    pass


class TodoShow(TodoBase):
    """
    This is model for response or getting todos
    """
    id: int
    added: datetime
    updated: datetime

    class Config:
        orm_mode = True