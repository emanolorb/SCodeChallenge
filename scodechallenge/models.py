import datetime

from sqlalchemy import (ARRAY, Boolean, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_request = Column(String)
    item_response = Column(ARRAY(Integer))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
