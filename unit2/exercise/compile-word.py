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
    if word.isupper():
        ops = [ str( 10**i ) + '*' + char for i, char in enumerate(word[::-1]) ]
        return '(' + '+'.join(ops) + ')'
    else:
        return word


print compile_word('I')
print compile_word('ME')
print compile_word('YOU')
print compile_word('YOUR')
