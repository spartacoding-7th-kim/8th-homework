import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

music_list = soup.select('.list-wrap > tbody > tr')
# print(music_list[0])
for music in music_list :
    rank_raw = music.select_one('td.number').text
    rank = rank_raw.split()
    title = music.select_one('input')['title']
    artist = music.select_one('a[class="artist ellipsis"]').text
    print(rank[0], title, artist)