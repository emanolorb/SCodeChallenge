import datetime
from typing import List, Optional

from pydantic import BaseModel, Json


class ItemBase(BaseModel):
    id: str
    item_request: Json
    item_response: Json
    created_date: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True

class RequestItem(BaseModel):
    items: Optional[
        List
    ] = []
