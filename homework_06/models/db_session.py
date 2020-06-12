from sqlalchemy.orm import sessionmaker, scoped_session
from homework_06.models.engine import Engine

# создание сессий для БД
session_factory = sessionmaker(bind=Engine)
Session = scoped_session(session_factory)
