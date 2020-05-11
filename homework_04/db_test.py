from homework_04.create_db import Author, Post, Session

# тест - названия по конкретному автору
def test_titles_by_author():
    session = Session()

    # узнаем id конкретного автора
    q_1 = session.query(Author).filter(Author.author == 'Л.Н. Андреев')
    author_id = q_1.one().id

    # выберем все его произведения
    q_2 = session.query(Post).filter(Post.author_id == author_id)
    res = q_2.all()
    # соберём их в список и сравним с известной информацией
    author_titles_list = []
    for r in res:
        author_titles_list.append(r.title)
    # print(author_titles_list)
    session.close()

    assert set(author_titles_list) == {'Красный смех', 'Елеазар'}


# тест - названия произведений, написанных в конкретный год
def test_titles_by_year():
    session = Session()

    # выберем все произведения конкретного года
    q_1 = session.query(Post).filter(Post.year == '1906')
    res = q_1.all()
    # соберём их в список и сравним с известной информацией
    titles_by_year_list = []
    for r in res:
        titles_by_year_list.append(r.title)
    print(titles_by_year_list)
    session.close()

    assert set(titles_by_year_list) == {'Хозяева жизни', 'Елеазар'}


# тест - имена авторов, написавших произведения в конкретный год
def test_authors_by_year():
    session = Session()

    # выберем id авторов, написавших произведения в конкретном году
    q_1 = session.query(Post).filter(Post.year == '1906')
    res = q_1.all()
    # соберём их в список для последующего запроса
    author_id_by_year_list = []
    for r in res:
        author_id_by_year_list.append(r.author_id)
    # print(author_id_by_year_list)

    # выберем имена авторов по id
    q_2 = session.query(Author).filter(Author.id.in_(author_id_by_year_list))
    res = q_2.all()
    # соберём их в список и сравним с известной информацией
    author_by_year_list = []
    for r in res:
        author_by_year_list.append(r.author)
    #print(author_by_year_list)
    session.close()

    assert set(author_by_year_list) == {'Л.Н. Андреев', 'А.М. Горький'}


# if __name__ == '__main__':
#     test_titles_by_author()
#     test_titles_by_year()
#     test_authors_by_year()
