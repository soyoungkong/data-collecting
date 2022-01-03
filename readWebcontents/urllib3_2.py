import urllib.request

res = urllib.request.urlopen("http://unico2013.dothome.co.kr/crawling/tagstyle.html")
print(res)
print("[header 정보] ------- ")
res_header = res.getheaders()
for s in res_header:
    print(s)
print("[body 정보] ------- ")
print(res.read())
#print(res.read().decode('utf-8)) #read와 read.decode 차이를 확인할 것