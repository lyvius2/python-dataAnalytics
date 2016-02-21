# -* coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup as bs
import requests

def write_csv(data, filename, delimiter=",", quotechar='"'):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, \
                            delimiter=delimiter,\
                            quotechar=quotechar)
        writer.writerows([[item.encode('utf-8') for item in row] for row in data])
        # [[item.encode('utf-8') for item in row] for row in data]
    return filename

def movie_crawler(url):
    res = requests.get(url)
    table = []
    if res.status_code == 200:
        soup = bs(res.text, 'html.parser')

        # movies1 = soup.select('#main > div > div.list.detail > div')
        # print movies1[0].attrs
        movies2 = soup.findAll('div',{'itemtype':'http://schema.org/Movie'})
        # print len(movies2)

        for movie in movies2:
            row = []
            titles = movie.findAll('h4',{'itemprop':'name'})
            scores = movie.select('div.rating_txt > div > strong')
            genres = movie.findAll('span',{'itemprop':'genre'})
            directors = movie.select('span[itemprop=director] > span > a')
            actors = movie.select('span[itemprop=actors] > span > a')
            title = titles[0].text.strip() if len(titles)>0 else ''
            score = scores[0].text.strip() if len(scores)>0 else ''
            genre = "/".join([genre.text for genre in genres])
            director = '|'.join([director.text for director in directors])
            actor = ', '.join([actor.text.strip() for actor in actors])
            row = [title, score, genre, director, actor]
            table.append(row)
    return table

data = movie_crawler('http://www.imdb.com/movies-coming-soon/2015-01')
print write_csv(data, 'movies.csv')