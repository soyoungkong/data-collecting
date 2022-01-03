import requests
r = requests.get("http://unico2013.dothome.co.kr/crawling/exam.html")
r.encoding = 'utf-8'
print(type(r))
if r.text:
    print(r.text)
else:
    print('응답된 콘텐츠가 없습니다.')

print("----------------------------------")
r = requests.head("http://unico2013.dothome.co.kr/crawling/exam.html")
r.encoding = 'utf=8'
print(type(r))
if r.text:
    print(r.text)
else:
    print('응답된 콘텐츠가 없어요.')

print("----------------------------------")
r = requests.post("http://unico2013.dothome.co.kr/crawling/post.php", data={'name': '백도', 'age': 12})
r.encoding = 'utf-8'
print(type(r))
if r.text:
    print(r.text)
else:
    print('응답된 콘텐츠가 없어요.')