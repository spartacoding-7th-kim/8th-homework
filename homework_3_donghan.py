from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

music_data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

#보기쉽게 파싱하기
soup = BeautifulSoup(music_data.text, 'html.parser')


#tr 불러모으기
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    rank = music.select_one('td.number').text.split()[0]
    title = music.select_one('td.info > a.title.ellipsis').text.split()
    title_split = ' '.join(title)
    singer = music.select_one('td.info > a.artist.ellipsis').text.split()
    singer_split = ' '.join(singer)
    print(rank, title_split, singer_split)