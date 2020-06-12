from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from homework_06.models.base import Base

# Класс для авторов произведений
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    author = Column(String(30), nullable=False)

    posts = relationship('Post', back_populates='author')