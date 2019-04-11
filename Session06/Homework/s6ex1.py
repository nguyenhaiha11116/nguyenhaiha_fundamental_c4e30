import requests
import bs4
from youtube_dl import YoutubeDL
import pyexcel

url = 'https://www.apple.com/itunes/charts/songs/'

response = requests.get(url)

bs = bs4.BeautifulSoup(response.content,'html.parser')
all_a_tag = bs.find('div',{'id':'main'})
abc = all_a_tag.find_all('li')
data_crawled = []
print(len(abc))
for v in abc:
    post = {}
    post['song'] = v.h3.a.string
    post['link'] = v.h3.a.attrs['href']
    post['artis'] = v.h4.a.string
    data_crawled.append(post)
print(data_crawled)

pyexcel.save_as(records=data_crawled, dest_file_name="s6ex1.xlsx")

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
}
for v in data_crawled:
    dl = YoutubeDL(options)
    dl.download([v['song']+v['artis']])