# Jessalyn Sebastian
# fair coin toss probability

import math

def choose(n, k):
    """ Computes n choose k, in combinatorics. The number of ways k elements can
be chosen from a set of n elements."""
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    

def compute_prob(nTrials, numObserved):
    """ Computes the probability of a fair coin showing numObserved heads
by chance if we toss it nTrials times """
    if type(nTrials)!= int or type(numObserved)!=int:
        print("Please enter two integers larger than 0")
        return
    if nTrials < 0 or numObserved < 0:
        print("Please enter two integers larger than 0")
        return
    if nTrials < numObserved:
        print("nTrials must be larger than numObserved")
        return
    return (choose(nTrials, numObserved))*((0.5)**(nTrials))
