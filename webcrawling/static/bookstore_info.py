import requests
from bs4 import BeautifulSoup

title = []
link = []

urlStr = 'http://www.yes24.com/SearchCorner/Search?domain=BOOK&query=python'
r = requests.get(urlStr)
r.encoding = "utf-8"  # 해당 페이지에 맞게 인코딩 해줌
bs = BeautifulSoup(r.text, 'html.parser')
titleList = bs.select('.lnk_key')
print(titleList)
print("--도서 제목--")
for titleDom in titleList:
    title.append(titleDom.string)
print(title)

linkList = bs.select('.lnk_key')
for linkDom in linkList:
    link.append(linkDom["href"])
print("--도서 링크 URL--")
print(link)



