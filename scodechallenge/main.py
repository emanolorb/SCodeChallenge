from fastapi import FastAPI, Depends
from . import item_crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Server on!"}


@app.post("/items/", response_model=schemas.ResponseItem)
def create_item(
    request_item: schemas.RequestItem, db: Session = Depends(get_db)
):
    return item_crud.create_item(db=db, request_item=request_item)


@app.get("/items/", response_model=List[schemas.ItemBase])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items
