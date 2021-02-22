import datetime
from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    id: str
    item_request: str = None
    item_response: List[int] = []
    created_date: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True

class RequestItem(BaseModel):
    items: Optional[
        List
    ] = []

class ResponseItem(BaseModel):
    result: List[int] = []
