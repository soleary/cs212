#!/usr/bin/python
# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is either '->' or '<-' to represent here-to-there or
# there-to-here motion.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    by '->' for here to there and '<-' for there to here."""
    here, there, t = state
    # your code here  

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    assert bsuccessors((frozenset([1, 2, 5, 10, 'light']), frozenset([]), 0)) == {
                (frozenset([1, 10]), frozenset(['light', 2, 5]), 5): (5, 2, '->'), 
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2): (2, 1, '->'), 
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5): (5, 5, '->'), 
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10): (5, 10, '->'), 
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2): (2, 2, '->'), 
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10): (10, 1, '->'), 
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10): (10, 10, '->'), 
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10): (10, 2, '->'), 
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5): (5, 1, '->'), 
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1): (1, 1, '->')}
    
    return 'tests pass'

print test()




