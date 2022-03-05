from bs4 import BeautifulSoup as bs
import requests as req
from requests import get
import time
import random
import lxml

url = 'https://www.youtube.com/watch?v=HL-99eCxSHw'
quotes = []
print(url)
response = get(url)
soup = bs(response.text, 'html.parser')
print(soup)

vid_info = soup.find('yt-formatted-string', class_="style-scope ytd-video-primary-info-renderer")
if vid_info != []:
    print(vid_info)
else:
    print('Not found')


