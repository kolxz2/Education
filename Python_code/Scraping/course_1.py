import requests
from bs4 import BeautifulSoup


# получаем html страничку
def get_html(url):
    # r - response ответ, отклик
    r = requests.get(url)
    # возращаем html текст страницы
    return r.text


def get_data(html):
    # проеобразуем html в объект Python
    soup = BeautifulSoup(html, 'lxml')
    # осуществляем поиск внутри траницы
    # изымаем нужные нам детали
    # h1 нам нужен, поэтому початям раскрываем html
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return h1


def main():
    url = 'https://wordpress.org/'
    # в парсер передаём наш html code
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()