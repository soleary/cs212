#!/usr/bin/python
#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

floors = bottom, _, _, _, top = [ 1, 2, 3, 4, 5 ]

def ishigher(f1, f2): return f1 > f2 

def notadjcent(f1, f2): return abs(f1 - f2) > 1

def floor_puzzle():
    orderings = list(itertools.permutations(floors))
    return next(
            [ Hopper, Kay, Liskov, Perlis, Ritchie ] 
            for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
            if Hopper is not top
            if Kay is not bottom
            if Liskov is not bottom
            if Liskov is not top
            if ishigher(Perlis, Kay)
            if notadjcent(Ritchie, Liskov)
            if notadjcent(Liskov, Kay)
            )

print floor_puzzle()
