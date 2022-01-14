# 요약 댓글과 상세 댓글(펼쳐보기)
# 한 페이지에 5개씩 댓글이 있음
from selenium import webdriver
driver = webdriver.Chrome('C:/tmp/chromedriver')
driver.implicitly_wait(3)

driver.get("http://www.yes24.com/Product/goods/40936880")

import time
time.sleep(2)   # time이 import 되는 동안 딜레이를 주어서 오류가 나지 않도록 한다.

readLinks = driver.find_elements_by_css_selector('#infoset_reivew div.btn_halfMore > a')     # 펼쳐보기
for readlink in readLinks :
    readlink.click()
    time.sleep(1)
reviewList = driver.find_elements_by_css_selector('#infoset_reviewContentList div.reviewInfoBot.origin div.review_cont')

temp_list = []
time.sleep(3)
for review in reviewList:
    print(review)
    temp_list.append(review.text)

stopFlag = False
while True:
    for n in range(4, 13):
        linkurl = '#infoset_reviewContentList > div.review_sort.sortBot > div.review_sortLft > div > a:nth-child('+str(n)+')'
        linkNum = driver.find_element_by_css_selector(linkurl)
        linkNum.click()
        time.sleep(3)
    readLinks = driver.find_elements_by_css_selector('#infoset_reviewContentList div.btn_halfMore > a')

    for readlink in readLinks:  # 각 다섯 개의 댓글 페이지가 있음. 펼쳐보기 링크
        readlink.click()
        driver.execute_script("arguments[0].click();", readlink)    # 자바스크립트 메소드인 execute_script를 사용. 실행오류를 줄이기 위해서
        time.sleep(3)

    reviewList = driver.find_elements_by_css_selector('#infoset_reviewContentList div.reviewInfoBot.origin div.review_cont')
    time.sleep(2)

    for review in reviewList:
        temp_list.append(review.text)
        if len(reviewList) < 5:    # 댓글의 갯수가 5개보다 작을 때 끝남
            stopFlag = True
            break

    if stopFlag:
        break

    nextPage = '#infoset_reviewContentList > div.review_sort.sortBot > div.review_sortLft > div > a.bgYUI.next'     # 다음페이지
    linkNum = driver.find_element_by_css_selector(nextPage)
    linkNum.click()
    time.sleep(1)

for item in temp_list:
    print(item)

wFile = open("c:/tmp/book comment file.txt", "w")
wFile.writelines(temp_list)
wFile.close()