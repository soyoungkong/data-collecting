from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/tmp/chromedriver')
driver.get('https://www.naver.com/')
# css 선택자 사용
# target = driver.find_element_by_css_selector("[name = 'query']")
# css 속성 사용
# target = driver.find_element_by_class_name("input_text")
# id 속성 사용
target = driver.find_element_by_id("query")
print("태그 객체 : ", type(target))
target.send_keys('자바')  # 검색어
target.send_keys(Keys.ENTER)
# driver.quit()
