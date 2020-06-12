from homework_06.models import Base

# создание базы данных
if __name__ == "__main__":
    Base.metadata.drop_all()
    Base.metadata.create_all()

