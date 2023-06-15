"""

"""

import numpy as np
from scipy.stats import binom

"""
Find the largest expected number of successes for "n" samples of a bernoulli distribution with probability "p"
subject to the requriement that the success rate for observing this event is at least c.
"""
def max_successes(p, n, c):
    # Start from the smallest number of successes and increment until overall success probability is reached
    k = 0

    # Check the CDF value for this number of successes
    cdf = 1-binom.cdf(k, n, p)
    if cdf < c:
        # print("No number of successes is possible with confidence {}".format(c))
        return 0

    # Search in the direction of higher successes if the CDF value is less than c
    while cdf > c:
        k += 1
        cdf = 1-binom.cdf(k, n, p)

    return k

"""
Calculate the minimum number of trials needed from a bernoulli distribution to ensure that at least "d"
successes occour with total success success rate at least "c"
"""
def min_trials(p, c, num_successes, inc=1):
    n = 0
    while max_successes(p, n, c) < num_successes:
        print(n, max_successes(p, n, c))
        n += inc
    return n

# Constants
p_e = 2.18e-4 # Success probability of end-to-end entanglement
p_p = 0.5 # Success probability of parity check purification
c = 0.999 # overall success probability
d = 30 # code distance

p = 2.18e-4
c = 0.999
num_successes = 1680
num_ions = min_trials(p, c, num_successes, inc=100000)

print("\nNumber of trapped-ions required = {}".format(num_ions))

