import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pymongo
from project.config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB_TB]

# browser = webdriver.Ie()
browser = webdriver.PhantomJS(executable_path='D:\Software\PlantomJS\phantomjs-2.1.1-windows\\bin\phantomjs.exe',service_args=SERVICE_ARGS)
wait = WebDriverWait(browser, 10)


def search():
    try:
        browser.get('https://www.taobao.com')
        input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#q')))[0]
        # submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#su')))
        input.send_keys('美食')
        # 淘宝网站找不到搜索按钮，使用 Keys.ENTER 代替
        input.send_keys(Keys.ENTER)
        # submit.click()
        total = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.total')))[0]
        get_products()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input.input:nth-child(2)')))[0]
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn:nth-child(4)')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li.active > span:nth-child(1)'), str(page_number)))
        get_products()
    except TimeoutException:
        return next_page(page_number)


def get_products():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE_TB].insert(result):
            print('save to mongodb success', result)
    except Exception as e:
        print(e)
        print('save to mongodb fail', result)


def main():
    try:
        total = search()
        total = int(re.compile(r'(\d+)', re.S).search(total).group(1))
        for i in range(2, total + 1):
            next_page(i)
        browser.close()
    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == '__main__':
    main()
