import datetime
from sqlalchemy.orm import Session
from .utils import getItemsList
from . import models, schemas


def create_item(db: Session, request_item: schemas.RequestItem):
    new_item = getItemsList(request_item.items)
    db_item = models.Item(
        item_request=str(request_item.items),
        item_response=new_item,
        created_date=datetime.datetime.now()
    )
    db.add(db_item)
    db.commit()
    return {
        'result': new_item
    }

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
