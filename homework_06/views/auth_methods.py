from werkzeug.exceptions import BadRequest
from flask import request

from homework_06.models import Session, User, Author, Post


# функции, используемые в разделе auth
# проверка имени пользователя и пароля
def validate_username_and_password(username, password):
    if not (
        username
        and len(username) >= 3
        and password
        and len(password) >= 8
    ):
        raise BadRequest("Username has to be at least 3 symbols and password at least 8")


# достать юзернейм и пароль
def get_username_and_password():
    username = request.form.get("username")
    password = request.form.get("password")
    validate_username_and_password(username, password)

    return username, password


# проверка уникальности юзернейма
def validate_username_unique(username: str):
    if Session.query(User).filter_by(username=username).count():
        raise BadRequest("Username already exists!")


# достать информацию об имеющихся произведениях
def title_list():
    session = Session()
    q_1 = session.query(Post)
    res = q_1.all()
    # соберём их в список и сравним с известной информацией
    titles = []
    for r in res:
        title_id = r.id
        title = r.title
        title_year = r.year
        q_2 = session.query(Author).filter(Author.id == r.id)
        for a in q_2.all():
            title_author = a.author
        titles.append([str(title_id), title, title_year, title_author])
    session.close()
    return titles


# достать текст произведения
def title_texts(title_id):
    session = Session()
    q_1 = session.query(Post).filter(Post.id == title_id)
    res = q_1.all()
    # соберём их в список и сравним с известной информацией
    for r in res:
        title_text = r.text
        title_name = r.title
    session.close()
    return title_text, title_name