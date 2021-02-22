import datetime
from sqlalchemy import (Boolean, Column, ForeignKey, Integer, String,
                        DateTime, ARRAY)
from sqlalchemy.orm import relationship
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_request = Column(ARRAY(Integer, ARRAY(Integer)))
    item_response = Column(ARRAY(Integer))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
