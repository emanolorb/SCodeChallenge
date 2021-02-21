import datetime
from sqlalchemy import (Boolean, Column, ForeignKey, Integer, String,
                        DateTime)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_request = Column('data', JSONB)
    item_response = Column('data', JSONB)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
