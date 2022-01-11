import requests
from bs4 import BeautifulSoup

login_html = 'https://www.hanbit.co.kr/member/login_proc.php'
crawl_html = 'http://www.hanbit.co.kr/myhanbit/myhanbit.html'

session_data = requests.session()

params = dict()
params['m_id'] = '아이디'
params['m_passwd'] = '비밀번호'

login = session_data.post(login_html, data=params)
login.raise_for_status()
login = session_data.get(crawl_html)
soup = BeautifulSoup(login.content, 'html.parser')
mileage = soup.select('dl.mileage_section1> dd > span')
for item in mileage:
    print("마일리지 :" + item.get_text())
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("이코인 :" + ecoin)
