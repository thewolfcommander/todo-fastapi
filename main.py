from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

from todo import (
    models, 
    database, 
    schemas, 
    handlers
)

# Creating all the tables in the database
models.Base.metadata.create_all(bind=database.engine)

# Creating instance on FastAPI Server
app = FastAPI()


# Connecting to the Database
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/todos/', response_model=schemas.TodoShow)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """
    API Endpoint to create new todo
    """
    return handlers.create_todo(db=db, todo=todo)


@app.get('/todos/')
def get_all_todos(start: int = 0, end: int = 100, db: Session = Depends(get_db)):
    """
    API Endpoint to get all todos
    """
    return handlers.get_all_todos(db, start=start, end=end)


@app.get('/todos/{todo_id}/')
def get_all_todos(todo_id: int, db: Session = Depends(get_db)):
    """
    API Endpoint to get a single todo
    """
    return handlers.get_todo_by_id(db, todo_id)


@app.put('/todos/{todo_id}/', response_model=schemas.TodoShow)
def update_todo(todo_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """
    API Endpoint to update the Todo
    """
    return handlers.update_todo(db, todo_id, todo)


@app.delete('/todos/{todo_id}/')
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """
    API Endpoint to update the Todo
    """
    instance = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(instance)
    db.commit()
    return todo_id