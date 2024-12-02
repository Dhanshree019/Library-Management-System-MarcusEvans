from sqlalchemy import *
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(length=100), nullable=False)
    email = Column(VARCHAR(length=100), unique=True, nullable=False)
    password = Column(VARCHAR(length=100), nullable=False)
    role = Column(VARCHAR(length=100), nullable=False)

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
            "password" : self.password,
            "role" : self.role
        }
    

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(length=100), index=True, unique=True)
    author = Column(VARCHAR(length=100))
    genre = Column(VARCHAR(length=100))
    availability = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default= datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return{
            "id" : self.id,
            "title" :self.title,
            "author" : self.author,
            "genre" : self.genre,
            "availability" : self.availability
        }