#!/usr/bin/python

def all_ints():
    n = 0
    yield n
    while 1:
        n += 1
        yield n
        yield -n

for i in all_ints():
    print i
    if i > 10:
        break
