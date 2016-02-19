# -*- coding: utf-8 -*-

# result = raw_input("무엇이든 입력해보세요 : ")
# print "당신이 입력한 내용은 {0}입니다".format(result)

import random

def number_game():
    answer = random.randrange(1,11) # 1~10
    life = 3

    while life > 0:
        user_input = raw_input("1부터 10까지 숫자를 맞춰보세요 (남은 목숨: {0}개) : ".format(life))
        int_user_input = int(user_input)
        if int_user_input == answer:
            print "정답입니다! 게임을 종료합니다."
            return
        elif int_user_input > answer:
            print "{0}보다 작습니다.".format(user_input)
            life -= 1
        elif int_user_input < answer:
            print "{0}보다 큽니다.".format(user_input)
            life -= 1

    print "정답은 {0}이었습니다. 아쉽군요.".format(answer)
    return

number_game()

# w : 파일 쓰기, r : 파일 읽기
f = open("/tmp/python_lecture.txt","w")
for i in range(1,11):
    text = "여기는 {0}번째 줄입니다.\n".format(i)
    f.write(text)
f.close()

f = open("/tmp/python_lecture.txt","r")
while True:
    line = f.readline()
    if not line:
        break
    print line
f.close()

def get_words_count(file_path):
    result = {}
    f = open(file_path, "r")
    while True:
        line = f.readline().replace("\"","")
        if not line:
            break
        for item in line.split():
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    f.close()
    return result

print get_words_count("./gatsby.txt")

