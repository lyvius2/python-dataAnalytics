# -*- coding: utf-8 -*-
import csv

with open('sample.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['검사외전','범죄','126분'])
    writer.writerow(['쿵푸팬더 (Kung fu Panda 3, 2016)','애니메이션','95분'])

data = []
with open('sample.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',',quotechar='|')
    for row in reader:
        data.append(row)

print data

for row in data:
    for item in row:
        print item