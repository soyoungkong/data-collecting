from bs4 import BeautifulSoup

html_doc = "<!DOCTYPE html>" \
           "<html>" \
           "    <head>" \
           "        <meta charset='utf-8'>" \
           "        <title>Test BeautifulSoup </title>" \
           "    </head>" \
           "    <body>" \
           "        <h1> 테스트 </h1>" \
           "    </body>" \
           "</html>"

bs = BeautifulSoup(html_doc, 'html.parser')
print("type: ", type(bs))
print("prettify: ", bs.prettify())  # 들여쓰기가 적용되어서 나옴
