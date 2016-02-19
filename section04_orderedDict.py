# -*- coding: utf-8 -*-

fruits = {
    "apple" : 3000,
    "lemon" : 5000,
    "melon" : 10000
}

print fruits

from collections import OrderedDict

ordered_fruits = OrderedDict(
    [("apple", 3000),
     ("lemon", 5000),
     ("melon", 10000)]
)
print ordered_fruits
print ordered_fruits["melon"]