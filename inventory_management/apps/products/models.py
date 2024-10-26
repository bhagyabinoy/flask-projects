from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()   


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    created = Column(DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    modified = Column(DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
   

