# -*- coding: utf-8 -*-
class Person():
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self, what_to_say):
        print "안녕하세요 내 이름은 {0}입니다, 하고 싶은 말은 {1}입니다.".format(self.name, what_to_say)


iu = Person("아이유", 23)
print iu.name
print iu.age
print iu.talk("반가워요")


# 상속
class Actor(Person):
    movies = []


tom = Actor("Tom Hanks", 60)
print tom.name
print tom.talk("what?")


class Movie():
    name = ""
    year = 1970

    def __init__(self, name, year):
        self.name = name
        self.year = year


some_movie = Movie("라이언 일병 구하기", 2000)
print some_movie.name, some_movie.year

tom.movies.append(some_movie)
tom.movies.append(Movie("캐스트 어웨이", 2001))
tom.movies.append(Movie("터미널", 2009))

for item in tom.movies:
    print item.name, item.year
