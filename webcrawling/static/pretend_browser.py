'''
 웹크롤링하려는 사이트에서 브라우저로부터의 요청인지 체크하여, 브라우저인 경우에만 정보를 전달함.
 요청 헤더 User-Agent(딕셔너리로 만듦) -> 지정 전달 -> 성공적인 크롤링
 '''

import json
import urllib.request

hdr = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                     'Chrome/96.0.4664.110 Safari/537.36'}
req = urllib.request.Request('https://github.com/soyoungkong/data-collecting', headers=hdr)
data = urllib.request.urlopen(req).read()
page = data.decode('utf-8', 'ignore')
print(page)