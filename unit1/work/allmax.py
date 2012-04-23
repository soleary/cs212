#!/usr/bin/python

def allmax(iterable, key=None):
    "Return a list of all items that equal the max in iterable"
    key = key or lambda (x): x
    mymax = max([ k for key(k) in iterable ])
    maxlist = []
    for i in iterable:
        if i == mymax: maxlist.append(i)

    return maxlist or None

testlist = [
    ( 8, 9, 8 ),
    ( 8, 9, 8 ),
    ( 7, 6, 4 ),
    ( 1, 2, 3 ),
]

print testlist

print allmax(testlist)
