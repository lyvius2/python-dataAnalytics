# -*- coding: utf8 -*-
from bs4 import BeautifulSoup as bs
import requests

target_url = 'http://www.imdb.com/movies-coming-soon/{0}'
movie_total = []

# for i in range(1,13):
#     date = '2015-' + str(i).zfill(2)
#     print '2015-' + str(i).zfill(2) + ' crawing..'
#     print target_url.format(date)

def crawl_movie_info(src):
    res = requests.get(src)
    if res.status_code == 200:
        soup = bs(res.text, 'html.parser')
        # title = soup.select('#main > div > div.list.detail > div > \
        # table > tbody > tr > td.overview-top > h4 > a')

        # titles = soup.find_all('h4', {
        #     'itemprop':'name'
        # })
        # movietime = soup.find_all('time', {
        #     'itemprop':'duration'
        # })
        # metascore = soup.select('div.metascore.no_ratings > strong')
        tables = soup.select('td.overview-top')


        print len(tables)
        # print tables[0].find('h4',{'itemprop':'name'}).text
        for table in tables:
            row = []
            title = table.find('h4',{'itemprop':'name'}).text
            metascore = table.select('div.metascore.no_ratings > strong')[0].text
            # movietime = table.find('time',{'itemprop':'duration'})
            print title + ':' + metascore



        # print movietime
        # for title in titles:
        #     print title.text



crawl_movie_info('http://www.imdb.com/movies-coming-soon/2015-01')

# for i in range(1,13):
#     date = '2015-' + str(i).zfill(2)
#     print target_url.format(date) + ' crawling...'
#     crawl_movie_info(target_url.format(date))
#     print target_url.format(date) + ' done.'
