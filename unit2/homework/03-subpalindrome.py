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

# Get the candiates
# for each candidate, expand window 2 chars, and apply
# if palindrome, repeat
# if not, return [ w, s, e ]
# sort returns by w (window)
# return largest value

import re

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    candidates = []
    for p in ('(.).\\1', '(.)\\1'):
        matches = re.finditer(p, text)
        candidates += [ [m.start(), m.end()] for m in matches ]

    print candidates
    palindromes = []
    for c in candidates:
        l = longest_palindrome(c[0], c[1], text)
        palindromes.append(l)

    if len(palindromes) > 0:
        print palindromes
        print "Returning ", max(palindromes)[1:]
        return max(palindromes)[1:]
    else:
        return 0, 0

def longest_palindrome(s, e, text):

    if s <= 0:
        e += 1
    elif e >= len(text):
        s -= 1
   
    string = text[s:e]
    if string == string[::-1]:
        return longest_palindrome(s - 1, e + 1, text)
    else:
        return [ e - s, s, e ]

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('caecarr') == (5, 7)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
