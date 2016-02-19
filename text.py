# -*- coding: utf-8 -*-

lyrics = "Yesterday, all my troubles seem so far away"

def count_alphabet(array):
    count = 0
    for n in array:
        if n=="e":
            count += 1
    return count

print count_alphabet(lyrics)

def double_alphabet(array):
    result = ''
    for n in array:
        result += n*2
    return result

print double_alphabet('Hello World~')

# 문자열 포매팅
fruits_text = "나는 {drink}를 마셨고 {food}를 먹었다."
print fruits_text.format(drink="사이다",food="피자")

def print_formatting(count):
    text = "{0}마리의 돼지가 {1}하고 웁니다."
    for n in range(1,count+1):
        print text.format(n, "꿀"*n)

print_formatting(9)

