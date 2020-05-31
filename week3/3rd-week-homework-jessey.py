import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers = headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    print(type(song.select_one('td.number')))
    rank = song.select_one('td.number').contents[0].strip() #contents는 파이썬의 내장 함수로, split()으로 빈칸 기준으로 나눠서 요소룰 구분해준다.
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank, title, artist)