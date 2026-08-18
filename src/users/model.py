from sqlalchemy import Column, String, Integer, DateTime, Boolean
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "user_table" 

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    hash_password = Column(String)
    email = Column(String)
