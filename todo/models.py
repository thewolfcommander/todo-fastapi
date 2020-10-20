from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from todo.database import Base


class Todo(Base):
    """
    Model for handling Todos
    """
    __tablename__ = "todos"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String(255), index=True)
    description = Column(String)
    added = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now)
    status = Column(String(50))