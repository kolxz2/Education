import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('course_3.csv', 'a') as f:
        # писатель
        writer = csv.writer(f)
        pass


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find('tbody').find_all('tr')
    print(len(trs))
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[2].find('div').find('p').text
        print(name)


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()