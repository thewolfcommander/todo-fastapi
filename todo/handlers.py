
from datetime import datetime
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


def get_todo_by_id(db: Session, todo_id: int):
    """
    Get a todo by ID
    """
    db_instance = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return db_instance


def update_todo(db: Session, todo_id: int, todo: schemas.TodoCreate):
    """
    Update todo by getting it by ID
    """
    db_instance = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db_instance.title = todo.title
    db_instance.description = todo.description
    db_instance.status = todo.status
    db_instance.updated = datetime.now()
    db.commit()
    db.refresh(db_instance)
    return db_instance


def delete_todo(db: Session, todo_id: int):
    """
    Delete todo by getting it by ID
    """
    db.query(models.Todo).filter(models.Todo.id == todo_id).delete()
    db.commit()
    
    return {}