from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf
8'>
<title>Test BeautifulSoup</title>
</head>
<body>
<p align="center"> text contents </p>
<p align="right" class="myp"> text contents 2 </p>
<p align="left" a="b"> text contents 3 </p>
<img src="http://unico2013.dothome.co.kr/image/
flower.jpg" width="500">
</body>
</html> 
"""

bs = BeautifulSoup(html_doc, 'html.parser')
print("----------------------------1. find, find_all 차이 ----------------------------")
print(type(bs.find('p')))
print(type(bs.find_all('p')))
print("----------------------------2. find ----------------------------")
print(bs.find('title'))
print(bs.find('p'))
print(bs.find('img'))
print("----------------------------3. find_all ----------------------------")
p_tags = bs.find_all('p')
print(p_tags)
print("----------------------------4. find_all for문 ----------------------------")
for tag in p_tags:
    print(tag)
print("----------------------------5. align, class로 찾기 ----------------------------")
print(bs.find('p', align="center"))
print(bs.find('p', class_="myp"))
print(bs.find('p', align="left"))
print("----------------------------6. attrs로 찾기----------------------------")
print(bs.find('p', attrs={"align": "center"}))
print(bs.find('p', attrs={"align": "right", "class": "myp"}))
print(bs.find('p', attrs={"align": "left"}))