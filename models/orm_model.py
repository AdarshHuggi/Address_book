
from database.db_connection import Base,engine
from sqlalchemy import create_engine, Column, Integer, Float,String,Boolean, ForeignKey, Text, TIMESTAMP,Date,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


class Address(Base):
    __tablename__ = 'address_book'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    town =Column(String,nullable=False)
    district = Column(String, nullable=True)
    state = Column(String,nullable=False)
    pincode = Column(Integer,nullable=False)
    country = Column(String, nullable=False)
    full_address =Column(String,)
    
 

Base.metadata.create_all(engine)