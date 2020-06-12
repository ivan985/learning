from sqlalchemy import create_engine

# Создание engine для БД
Engine = create_engine("sqlite:///myblog.db")
