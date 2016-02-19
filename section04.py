# -*- coding: utf-8 -*-

# import util
#
# result = util.sum_func(1,2,3,4,5)
# print result
#
# print util.echo_func("I want you")

# from util import sum_func, echo_func
#
# print sum_func(1,2,3)
# print echo_func("안녕하세요")

from datetime import datetime, timedelta

# print datetime.now()
#
# now = datetime.now()
# dt = timedelta(hours=12, minutes=30)
#
# print now - dt
#
# formatted_now = now.strftime("오늘은 %Y년 %m월 %d일(%a) %p %I시 %M분 %S 초입니다.")
#
# print formatted_now

def calDate(n):
    executeDay = (datetime.now() + timedelta(days=int(n))).strftime("{0}일 후 그 날은 %Y년 %m월 %d일입니다.".format(n))
    return executeDay

param = raw_input("숫자를 입력하세요 : ")
print calDate(param)

