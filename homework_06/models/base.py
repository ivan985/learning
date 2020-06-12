from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from homework_06.models.engine import Engine

# Описание базы данных
class Base:
    @declared_attr
    def __tablename__(self):
        return f"myblog_{self.__name__.lower()}"

    id = Column(Integer, primary_key=True)


Base = declarative_base(bind=Engine, cls=Base)
