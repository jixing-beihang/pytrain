from selenium import webdriver

browser = webdriver.PhantomJS(executable_path='D:\Software\PlantomJS\phantomjs-2.1.1-windows\\bin\phantomjs.exe')
html = browser.get('https://www.baidu.com')
print(html)