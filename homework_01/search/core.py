import requests
from bs4 import BeautifulSoup, SoupStrainer

def search(links_count, url, how_many_links):
    r = requests.get(url)
    # парсинг страницы
    soup = BeautifulSoup(r.content, 'html.parser', parse_only=SoupStrainer('a'))

    for a in soup.find_all('a', href=True):
        # достаём строку, содержащую ссылку
        link_in_str = str(a['href'])

        # проверяем, является ли ссылка прямой и не внутренней для поисковика
        if link_in_str.find('https') != -1:
            # выделяем текст ссылки
            link = link_in_str[link_in_str.find('https'):]
            # выделяем имя ссылки
            link_name = link[8:]
            link_name = link_name[:link_name.find('/')].replace('www.', '')

            # убираем внутренние ссылки поисковой системы
            if link_name.find('google') == -1:
                links_count = links_count + 1
                print(links_count, link_name, link)\

            # проверяем, не достигнуто ли нужное количество ссылок
            if links_count == how_many_links:
                return links_count

    # возвращаем текущее количество ссылок
    return links_count


def main_search():
    text = input('What we are going to search? Enter here: ')
    how_many_links = int(input('How many links? Enter here: '))
    current_page, links_count = 0, 0
    while links_count < how_many_links:
        # формируем ссылку на общую страницу поиска
        cur_url = 'https://www.google.ru/search?q=' + text + '&start=' + str(current_page) + '0'
        old_links_count = links_count
        links_count = search(links_count, cur_url, how_many_links)
        # проверка на случай, если ссылок найдено меньше, чем было задано
        if links_count == old_links_count and links_count < how_many_links:
            print('We have only ' + str(links_count) + ' links. End of programm.')
            break
        current_page = current_page + 1

