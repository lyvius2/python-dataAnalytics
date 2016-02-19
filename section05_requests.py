# -*- coding: utf8 -*-
from bs4 import BeautifulSoup as bs
import requests

res = requests.get('https://pixabay.com/en/')
print dir(res)

print res.status_code
# print res.text

soup = bs(res.text, 'html.parser')
imgList = soup.find_all('img')
# print imgList[0].attrs['src']

import urllib
def download_image(img_src, filename):
    res = urllib.urlretrieve(img_src, filename)
    return res

# download_image('https://pixabay.com'+imgList[1].attrs['src'], 'test.jpg')

print len(imgList)
for item in imgList:
    image_src = 'https://pixabay.com' + item['src']
    print image_src.split('/')[-1] + ' downloading...'
    download_image(image_src, image_src.split('/')[-1])
