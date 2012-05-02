#!/usr/bin/python
# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    spaces = text.find(' ')
    if spaces % 2 == 1:
        print "Found it"
        splitpos = spaces / 2 + 1

    end = window = len(text)
    startpos = 0
    while window > 1:
        string = text[startpos:startpos+window].lower()
        print string + ' <=> ' + string[::-1]
        if string == string[::-1]:
            return startpos, startpos + window

        if startpos + window == end:
            window -= 1;
            startpos = 0;
        else:
            startpos += 1;

    return 0, 0

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
