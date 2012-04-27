#!/usr/bin/python

# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

import re

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if re.findall('[A-Z]', word) == len(word):
        return word

    place = 1
    ops = []
    for char in reversed(word):
        ops.append( str(place) + '*' + char )
        place = place * 10

    return '(' + '+'.join(ops) + ')'


print compile_word('I')
print compile_word('ME')
print compile_word('YOU')
print compile_word('YOUR')
