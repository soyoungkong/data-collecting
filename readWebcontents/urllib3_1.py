import urllib.request

res = urllib.request.urlopen("http://www.naver.com/")
print(type(res))
print(res.status)
print(res.version) # 버젼 속성값
print(res.msg)
res_header = res.getheaders()

print("[header 정보] ------- ")
for s in res_header :
    print(s)