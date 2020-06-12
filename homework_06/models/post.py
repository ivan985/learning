from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from homework_06.models.base import Base
from .author import Author

# класс для постов (произведений)
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    # идентификатор автора
    author_id = Column(Integer, ForeignKey(Author.id), nullable=False)
    # название произведения
    title = Column(String(40), nullable=False)
    # текст проивзедения (для тестовой базы данных - фрагмент произведения)
    text = Column(Text, nullable=False)
    # год написания произведения, может быть неизвестен или нуждаться в комментарии
    year = Column(String(40), nullable=False)

    author = relationship(Author, back_populates='posts')

    # def __repr__(self):
    #     return f'<Text #{self.id} {self.title} {self.year}>'

