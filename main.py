# -*- coding: utf-8 -*-

coffee_menu = [
    {
        "name": "아메리카노",
        "price": 4000
    },
    {
        "name": "카페라떼",
        "price": 5000
    },
    {
        "name": "카페모카",
        "price": 6000
}]

def calculate_total_price(orderList):
    result = 0
    for menu in orderList:
        for drink in coffee_menu:
            if drink["name"] == menu:
                result += drink["price"]
    return result

print(calculate_total_price(["카페라떼","아메리카노"]))

# if + for문 활용법

fruits = ["사과","감귤","포도"]
if "포도" in fruits:
    print "포도 존재함"

def sum_func(a,b):
    return a+b

fun = sum_func

print sum_func

a = 1
print type(a)
print type(sum_func)
print fun(1,12)

def factorial_for(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print factorial_for(5)

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n-1)

print factorial(7)

# 재귀호출을 사용한 피보나치 수열 0, 1, 1, 3, 4, 8, 13 ...
def fib(n):
    if(n<2):
        return n
    else:
        return fib(n-2) + fib(n-1)

print fib(10)

# 가변길이 매개변수
def var_sum_func(*nums):
    result = 0
    for n in nums:
        result += n
    return result

print var_sum_func(1,2,3,4,5,12,24)

# List Comprehension
sum_price = 0
prices = [1000,2000,3000,4000,5000]

sum_price = sum([n for n in prices])
print sum_price

double_price = [price*2 for price in prices]
print double_price

input = [1, 3, 5, 7, 9, 3, 4, 5]
output = [n if n%2==0 else n*2 for n in input]

print output


def can_travel(is_weekday,is_vacation):
    if not is_weekday or is_vacation:
        return True
    else:
        return False
# 2의 2승
print 2**2
