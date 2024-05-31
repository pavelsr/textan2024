import math
import numpy as np
# inspired by https://stackoverflow.com/questions/2413522/weighted-standard-deviation-in-numpy

results = '''
70
10
10
90
60
80
40
50
20
30
40
80
40
100
70
10
30
30
80
90
'''

def rm_empty(lst):
    return [ int(x) for x in lst.split("\n") if x ]

def weighted_avg_and_std(values, weights):
    """Return the weighted average and standard deviation."""
    average = np.average(values, weights=weights)
    variance = np.average((values-average)**2, weights=weights)
    return (average, math.sqrt(variance))

results = rm_empty(results)
results = { key: value for key, value in enumerate(results,1) }
answ = weighted_avg_and_std( list(results.keys()), list(results.values()) )
print (answ)
