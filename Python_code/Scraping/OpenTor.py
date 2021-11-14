from selenium.common.exceptions import NoSuchElementException
from tbselenium.tbdriver import TorBrowserDriver
import time
import random
import os
import psycopg2 as pg2

# TODO добавить куки
# TODO аутификация соцсетей

skrl = True


def bd_conect() -> str:
    conn = pg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='postgres',
        database='yandex_url'
    )
    with conn.cursor() as cursor:
        cursor.execute(
            """SELECT article_url FROM article_urls ORDER BY random()"""
        )
        return cursor.fetchone()[0]


def opentor(url):
    with TorBrowserDriver("/home/nik/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US") as driver:
        windows_size(driver)
        driver.get(url)
        time.sleep(1)
        like(driver)
        if skrl:
            scroll(driver)
        driver.close()


def windows_size(driver):
    random_size = random.randrange(8)
    if random_size == 0:
        driver.set_window_size(1024, 768)
    elif random_size == 1:
        driver.set_window_size(1366, 768)
    elif random_size == 2:
        driver.set_window_size(800, 600)
    elif random_size == 3:
        driver.set_window_size(640,	360)
    elif random_size == 4:
        driver.set_window_size(320, 400)
    elif random_size == 5:
        driver.set_window_size(640, 480)
    elif random_size == 6:
        driver.set_window_size(720, 576)
    elif random_size == 7:
        driver.set_window_size(720, 480)


def scroll(driver):
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 2):
        driver.execute_script("window.scrollTo(0, {});".format(i))
        time.sleep(0.05)
    time.sleep(10)
    skrl = False


def like(driver):
    do_not = random.randrange(3)
    if do_not == 1:
        try:
            driver.find_element_by_xpath('//*[@id="article__left"]/div/div/div/div/button[1]').click()
        except NoSuchElementException:
            try:
                driver.find_element_by_xpath(
                    '//*[@id="article__page-root"]/main/div[1]/div[8]/div/div[3]/div[2]/div[2]/button[1]').click()
            except NoSuchElementException:
                scroll(driver)


def port9050():
    os.system('echo %s|sudo -S %s' % ("fedora21", "service tor restart"))


def main():
    try:
        while True:
            url = bd_conect()
            opentor(url)
    except EOFError:
        main()


if __name__ == '__main__':
    port9050()
    main()

# sudo service tor restart
