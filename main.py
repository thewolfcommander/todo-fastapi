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