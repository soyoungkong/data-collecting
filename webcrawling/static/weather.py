from bs4 import BeautifulSoup
import urllib.request as req
import io
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "C:/tmp/forecast.xml"
req.urlretrieve(url, savename)
xml = open(savename, "r", encoding="utf-8").read() #xml은 기본적으로 utf-8로 작성됨.
soup = BeautifulSoup(xml, 'html.parser')
info = {}
weather = []
for location in soup.find_all("location"):
    loc = location.find('city').string
    min_w = location.find_all('tmn')
    max_w = location.find_all('tmx')
    weather = ([a.string+"~"+b.string for a, b in zip(min_w, max_w)]) #zip함수로 한 쌍으로 만들어준다.
    if not (loc in info):
        info[loc] = []

    for data in weather:
        info[loc].append(data)

print(info)

with open('C:/tmp/forecast.txt', "wt", encoding="utf8") as f:
    for loc in sorted(info.keys()):
        f.write(str(loc)+'\n')
        for name in info[loc]:
            f.write('\t'+str(name)+'\n')
