# -* coding : utf-8 -*-
a = -3
print abs(a)

fruits = {
    'grape' : 10000,
    'apple' : 3000,
    'watermelon' : 17000
}
print fruits

print divmod(10, 3)

for i, key in enumerate(fruits):
    print i, key, fruits[key]

a = [1,2,3,4,5]
def make_double(x):
    return x*2

print map(make_double, a)
print [x*2 for x in a]

# Sort
a = [1,4,5,6,8,2,3,11,10]
asc_sorted = sorted(a)
desc_sorted = sorted(a, reverse=True)
print asc_sorted
print desc_sorted

a = 1
b = [1,2,3]
c = "hi"
def d():
    print "hello!"

print type(a)
print type(b)
print type(c)
print type(d)

temp = sorted(fruits)