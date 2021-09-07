import requests # для гет запрсов http
from lxml import etree
import lxml.html
import csv


def parser(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    for i in range(len(text_original)):
        print(text_original[i], text_translate[i])


def main():
    parser("https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html")


if __name__ == "__main__":
    main()
