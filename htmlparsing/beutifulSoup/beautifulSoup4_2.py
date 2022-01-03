from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
    <html>
        <head>
            <meta charset='utf-8'>
            <title>Test BeautifulSoup</title>
        </head>
        <body>
            <p align="center">P 태그의 콘텐츠 </p>
            <img src="http://unico2013.dothome.co.kr/image/flower.jpg" width="300"/>
        <ul>
            <li> 테스트 1<strong> 강조 </strong></li>
            <li> 테스트 2</li>
            <li> 테스트 3</li>
        </ul>
        </body>
    </html> """

bs = BeautifulSoup(html_doc, 'html.parser')

print(type(bs.title), ':', bs.title)
print(type(bs.title.name), ':', bs.title.name)
print(type(bs.title.string), ':', bs.title.string)
print('----------------')
print(type(bs.p['align']), ':', bs.p['align'])
print(type(bs.img['src']), ':', bs.img['src'])
print(type(bs.img.attrs), ':', bs.img.attrs)
print('----------------')
print("[ string 속성 ]")  # 스트링 속성은 하나의 문자열로 구성된 경우에만 뽑을 수 있다.
print(type(bs.p.string), ':', bs.p.string)
print(type(bs.ul.string), ':', bs.ul.string)
print(type(bs.ul.li.string), ':', bs.ul.li.string)
print(type(bs.ul.li.strong.string), ':', bs.ul.li.strong.string)
print('----------------')
print("[ text 속성 ]") # 모든 텍스트를 뽑을 수 있음.
print(type(bs.p.text), ':', bs.p.text)
print(type(bs.ul.text), ':', bs.ul.text)
print(type(bs.ul.li.text), ':', bs.ul.li.text)
print(type(bs.ul.li.strong.text), ':', bs.ul.li.strong.text)
print('----------------')
print("[ contents 속성]") # 리스트 객체로 추출된다. 
print(type(bs.p.contents), ':', bs.p.contents)
print(type(bs.ul.contents), ':', bs.ul.contents)
print(type(bs.ul.li.contents), ':', bs.ul.li.contents)
print(type(bs.ul.li.strong.contents), ':', bs.ul.li.strong.contents)