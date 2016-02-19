# -*- coding: utf8 -*-
from bs4 import BeautifulSoup as bs

soup = bs(open('./index.html'), 'html.parser')

# print soup.title
# print soup.title.name
# print soup.title.text
# print soup.title.parent.name
# print soup.p
#
# print soup.find_all('a')
#
# print soup.select('.desc-box')
desc_line = soup.findAll('div',{'class':'desc-line'})
# print desc_line[0].parent
print desc_line[0].text
print desc_line[0].attrs

print soup.select('body > div > div > img')[0].attrs