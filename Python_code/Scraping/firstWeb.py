import requests  # для гет запрсов http
from PIL.XVThumbImagePlugin import r
from lxml import etree
import lxml.html
import csv
import time
from requests import Response


def parser(url):
    try:
        # TODO Исправить SSL на  Fedora
        ran = requests.get(url,  verify=False)
        print(ran.status_code())
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    tree = lxml.html.document_fromstring(ran.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    for i in range(len(text_original)):
        print(text_original[i], text_translate[i])


def main():
    parser('http://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html')


if __name__ == "__main__":
    main()
