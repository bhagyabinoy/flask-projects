from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()   


class User(Base):
    __tablename__ = "users"

   
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(24), nullable=True, index=True)
    last_name = Column(String(24),  nullable=True, index=True)
    username = Column(String(24), unique=True, index=True)
    password = Column(String(20), nullable=False, server_default='')
    email = Column(String(255), unique=True, index=True, nullable=False,
                      server_default='')
    created = Column(DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    
