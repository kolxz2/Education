import requests
from bs4 import BeautifulSoup
import csv


def get_url(url):
    r = requests.get(url)
    return r.text


def refind(s):
    reiting = s.split(' ')[0]
    result = reiting.replace(',', '')
    return result


def write_csv(data):
    # создаём файл и открываем его для записи путём стека и работаем через переменную f
    with open('course_2.csv', 'a') as f:
        writer = csv.writer(f)
        # принимет только один аргумент или картеж,
        # или список из нескольких элементов
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # find_all возвращает список из всех подходящих запросу
    section = soup.find_all('section')[1]
    # т.к. все плагины разделяются на articlrs, создаём
    # список из элементов
    plagins = section.find_all('article')
    for plagin in plagins:
        # вывели текст заголовка
        name = plagin.find('h3').text
        # получаем ссылку. find находит заголовки, то что после '<'
        url = plagin.find('h3').find('a').get('href')
        rating = refind(plagin.find('span', class_='rating-count').find('a').text)
        # создали словарь для записи в CSV
        data = {'name': name,
                'url': url,
                'reviews': rating}
        write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_url(url))


if __name__ == '__main__':
    main()