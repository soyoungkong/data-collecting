from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/tmp/chromedriver')
print("webdriver 객체 : ", type(driver))
driver.get('http://www.google.com/ncr')
target = driver.find_element_by_css_selector("[name = 'q']")
print("태그 객체 : ", type(target))
target.send_keys('파이썬')  #검색어 
target.send_keys(Keys.ENTER)
#driver.quit()