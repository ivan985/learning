from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
# импортируем словарь, содержащий тексты произведений
from homework_04.texts import text_dict

Engine = create_engine('sqlite:///myblog.db')
Base = declarative_base(bind=Engine)

session_factory = sessionmaker(bind=Engine)
Session = scoped_session(session_factory)


# Класс для авторов произведений
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    author = Column(String(30), nullable=False)

    posts = relationship('Post', back_populates='author')

    # def __repr__(self):
    #     return f'<Author #{self.id} {self.author}>'


# Класс для опубликованных в виде постов произведений
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

    def __repr__(self):
        return f'<Text #{self.id} {self.title} {self.year}>'


# функция для заполнения таблицы начальными тестовыми данными
def create_users_posts():
    session = Session()

    author_1 = Author(author='А.И. Тургенев')
    session.add(author_1)
    author_2 = Author(author='Л.Н. Андреев')
    session.add(author_2)
    author_3 = Author(author='А.М. Горький')
    session.add(author_3)
    session.flush()

    post_1 = Post(
        author_id=author_1.id,
        title='Отцы и дети',
        text=text_dict['Отцы и дети'],
        year='1862'
    )
    post_2 = Post(
        author_id=author_2.id,
        title='Красный смех',
        text=text_dict['Красный смех'],
        year='1904'
    )
    post_3 = Post(
        author_id=author_2.id,
        title='Елеазар',
        text=text_dict['Елеазар'],
        year='1906'
    )
    post_4 = Post(
        author_id=author_3.id,
        title='Хозяева жизни',
        text=text_dict['Хозяева жизни'],
        year='1906'
    )
    post_5 = Post(
        author_id=author_3.id,
        title='Городок Окуров',
        text=text_dict['Городок Окуров'],
        year='1909'
    )

    session.add(post_1)
    session.add(post_2)
    session.add(post_3)
    session.add(post_4)
    session.add(post_5)

    session.commit()
    session.close()


# создание базы данных
def main():
    # удалим старую версию базы данных
    Base.metadata.drop_all()
    # создадим текущую версию базы данных
    Base.metadata.create_all()
    # заполним базу данных тестовыми данными
    create_users_posts()
    # engine.dispose()


if __name__ == '__main__':
    main()
