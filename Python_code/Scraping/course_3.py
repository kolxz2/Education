import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def price_conv(price):
    p = price.replace(',', '')
    return p.replace('$', '')


def write_csv(data):
    with open('course_3.csv', 'a') as f:
        # писатель
        writer = csv.writer(f)
        writer.writerow([data['name'],
                         data['tiker'],
                         data['link'],
                         data['price']])


def name_tik(tds):
    try:
        name = (tds[2].find('div').find('p').text)
        tik = tds[2].find('div').find('p',
                    class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text
        link = 'https://coinmarketcap.com/' + tds[2].find('a').get('href')
        price = price_conv(tds[3].find('a').text)
    except AttributeError:
        try:
            nameTik = (tds[2].find('a').find_all('span'))
            tik = nameTik[2].text
            name = nameTik[1].text
            link = 'https://coinmarketcap.com/' + tds[2].find('a').get('href')
            price = price_conv(tds[3].find('span').text)
        except AttributeError:
            print('some Error')
    return name, tik, link, price


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find('tbody').find_all('tr')
    i = 1
    for tr in trs:
        tds = tr.find_all('td')
        all_data = name_tik(tds)
        data = {'name': all_data[0],
                'tiker': all_data[1],
                'link': all_data[2],
                'price': all_data[3]}
        write_csv(data)
        i += 1


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))
    print("Поздравляю, у тебя создаля файл CSV, \n"
          "который ты можешь открыть в EXEL. \n"
          "Файл course_3.csv находится в той же папке, \n"
          "где исполняемый файл course_3.py\n"
          "Если хочешь обновить данные в CSV,\n"
          "удали старый или же новые данные будут \n"
          "записываться под старыми")


if __name__ == '__main__':
    main()