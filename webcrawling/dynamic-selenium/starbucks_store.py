import urllib.request
from bs4 import BeautifulSoup
# 서버 접속
url = "https://www.starbucks.co.kr/store/store_map.do"
server = urllib.request.urlopen(url)
response = server.read().decode()
bs = BeautifulSoup(response, "html.parser")
li = bs.find_all('li', class_="quickResultLstCon")
print(li)
## 동적 페이지이므로 결과가 나오지 않음.

from selenium import webdriver
driver = webdriver.Chrome('C:/tmp/chromedriver')
driver.implicitly_wait(3)
driver.get(url)
target = driver.find_element_by_class_name("quickResultLstCon") #quickResultLstCon라는 클래스명을 가진 것을 찾음 
print(type(target))
print(type(target.text))
print(target.text)
driver.quit()
