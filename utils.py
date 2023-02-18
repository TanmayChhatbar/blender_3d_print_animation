# helper functions for path_follower
from math import sqrt
import numpy as np

def find_coord(line, curcoord):
    # find coordinate in line
    nl = curcoord.copy()
    checks = ["X", "Y", "Z", "F"]
    for i in range(len(checks)):
        if checks[i] in line:
            nl[i] = line.split(checks[i])[1].split(' ')[0].strip()
    return nl

def dis(loc1, loc2):
    # find euler distance
    return sqrt(sum((np.array(loc1)-np.array(loc2))[0:3]**2))
