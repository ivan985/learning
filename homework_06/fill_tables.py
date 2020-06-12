from homework_06.models import Session, Author, Post
from homework_06.models.texts import text_dict


# заполнение базы данных
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


if __name__ == "__main__":
    create_users_posts()
