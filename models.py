from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class LocationModel(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    barcode = Column(String)
    description = Column(String)

class BookModel(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    isbn = Column(String, unique=True)
    title = Column(String)

    location_id = Column(Integer, ForeignKey("location.id"))
    location = relationship(LocationModel)
