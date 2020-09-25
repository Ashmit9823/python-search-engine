from selenium import webdriver
import time
import mechanize
#change the url as per your location in wamp server and copy php file to your folder which wamp runs on. 
url = "http://localhost/search_engine_trig.php"
n = 0
ask = input('enter your query here: ')
path = "C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)

br = mechanize.Browser()
br.open(url)
br.select_form(nr=0)
br.form['query'] = ask
br.submit()

url_opening = br.geturl()
driver.get(url_opening)
google_serch = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
stop = input('type exit to exit it: ')
if stop == 'exit':
    quit()
