import requests
from bs4 import BeautifulSoup
import re

movie_grade = []
movie_review = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/96.0.4664.110 Safari/537.36 '
}

for n in range(1, 6):
    req = requests.get('https://movie.daum.net/moviedb/grade?movieId=3126&type=netizen&page=' + str(n), headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    grades = soup.select('.ratings')
    reviews = soup.select('.desc_txt')
    for dom in grades:
        movie_grade.append(dom.text)
    for dom in reviews:
        movie_review.append(dom.text.strip())

commentLength = len(movie_grade)
for i in range(commentLength):
    if len(movie_review[i]) != 0:
        print(movie_grade[i] + "\t" + movie_review[i])
