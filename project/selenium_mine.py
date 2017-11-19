import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# FireFox
# browser = webdriver.Firefox(executable_path='D:\Software\Firefox\geckodriver\geckodriver.exe')
# IE
browser = webdriver.Ie(executable_path='D:\Software\IEDriver_32\IEDriverServer.exe')
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    # 输入文字
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    # 显示等待
    wait = WebDriverWait(browser,10)
    wait.until(expected_conditions.presence_of_all_elements_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)

except Exception as e:
    print(e)
finally:
    browser.close()

# browser.get('https://www.taobao.com')
# # # 获取单个元素
# input = browser.find_element_by_id('q')
# input_second = browser.find_element(By.ID, 'q')
# input.send_keys('iphone')
# time.sleep(1)
# input.clear()
# input.send_keys('ipad')
# wait = WebDriverWait(browser, 10)
# # button = browser.find_element_by_class_name('btn-search')
# button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# button.click()

# 获取列表
# lis = browser.find_element_by_css_selector('.service-bd li')
# lis_second = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(lis,lis_second)
# browser.close()

# 获取属性
# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

# 获取文本内容
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_id('zu-top-add-question')
# print(input)
# print(input.text)
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# 搜索知乎
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_id('q')
# input.send_keys('china')
# wait = WebDriverWait(browser, 10)
# try:
#     button = wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'zu-top-search-button')))
#     print(button)
#     button.click()
# except TimeoutError as e:
#     print(e)
# except Exception as e:
#     print(e)
# finally:
#     browser.close()

# Cookies
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'test':'name','value':'value'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


# 选项卡管理
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')

