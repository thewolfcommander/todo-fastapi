from sqlalchemy.orm import Session

from todo import models, schemas


def create_todo(db: Session, todo: schemas.TodoCreate):
    """
    Create new todo using this handler
    """
    db_instance = models.Todo(**todo.dict())
    db.add(db_instance)
    db.commit()
    db.refresh(db_instance)
    return db_instance


def get_all_todos(db: Session, start: int = 0, end: int = 100):
    """
    Get all todos using this handler
    """
    return db.query(models.Todo).offset(start).limit(end).all()