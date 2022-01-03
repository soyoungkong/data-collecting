import urllib.request
print("=================")
url='http://www.python.org'
f = urllib.request.urlopen(url)
print(type(f))
print(type(f.info()))
encoding = f.info().get_content_charset()
print(url, '페이지 인코딩 : ', encoding)
text = f.read(500).decode(encoding)
print(text)
print("=================")
