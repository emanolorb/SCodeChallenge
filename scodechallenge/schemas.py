from typing import List, Optional

from pydantic import BaseModel, Json


class ItemBase(BaseModel):
    id: str
    item_request: Json
    item_response: Json
    created_date: Optional[datetime] = None

    class Config:
        orm_mode = True

class RequestItem(UserBase):
    items: Optional[
        List[
            Optional[List[int]], Optional[int]
        ]
    ] = []
