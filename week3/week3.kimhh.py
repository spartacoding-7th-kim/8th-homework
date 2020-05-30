import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)

selector_path = '#body-content > div.newest-list > div > table > tbody > tr'


soup = BeautifulSoup(response.text, 'html.parser')

musics = soup.select(selector_path)


for music in musics:

    rank = music.select_one('td.number').contents[0].strip()

    title = music.select_one('td.info > a.title').text.strip()
    artist = music.select_one('td.info > a.artist').text.strip()

    print(rank, title, artist)