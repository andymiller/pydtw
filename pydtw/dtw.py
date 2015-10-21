import numpy as np
import cutil


#############################################################
# (vectorized) distance functions for point-point distances #
#############################################################
def abs_dist(x, y):
    return np.sum(np.abs(x-y), axis=2)

def sq_dist(x, y):
    return np.sum((x-y)**2, axis=2)


#####################
# Main DTW function #
#####################
def dtw(x, y, dist=abs_dist):
    """Main dynamic time warping function, computes dist of two sequences

    Args:
        x    : nd array, T1 x D
        y    : nd array, T2 x D
        dist : function returns  
    :param func dist: distance used as cost measure (default L1 norm)

    Returns the minimum distance, the accumulated cost matrix and the wrap path.

    """
    x = np.array(x)
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
    y = np.array(y)
    if len(y.shape) == 1:
        y = y.reshape(-1, 1)

    # store length of each sequence
    r, c = len(x), len(y)

    D = np.zeros((r + 1, c + 1))
    D[0, 1:] = np.inf
    D[1:, 0] = np.inf

    # handle pairwise dist calculation w/ broadcasting
    D[1:, 1:] = dist(x[:, None, :], y[None, :, :])

    # sum up distance from neighboring cells
    #for i in range(r):
    #    for j in range(c):
    #        D[i+1, j+1] += min(D[i, j], D[i, j+1], D[i+1, j])
    cutil.min_cumsum(D)  # cythonized version

    D = D[1:, 1:]
    dist = D[-1, -1] / sum(D.shape)
    return dist, D, _trackeback(D)


def _trackeback(D):
    i, j = np.array(D.shape) - 1
    p, q = [i], [j]
    while (i > 0 and j > 0):
        tb = np.argmin((D[i-1, j-1], D[i-1, j], D[i, j-1]))

        if (tb == 0):
            i = i - 1
            j = j - 1
        elif (tb == 1):
            i = i - 1
        elif (tb == 2):
            j = j - 1

        p.insert(0, i)
        q.insert(0, j)

    p.insert(0, 0)
    q.insert(0, 0)
    return (np.array(p), np.array(q))


#############################################
#  Slow dynamic time warping code for tests #
#############################################
from numpy.linalg import norm
def slow_dtw(x, y, dist=lambda x, y: norm(x - y, ord=1)):
    """ Computes the DTW of two sequences.

    :param array x: N1*M array
    :param array y: N2*M array
    :param func dist: distance used as cost measure (default L1 norm)

    Returns the minimum distance, the accumulated cost matrix and the wrap path.

    """
    x = np.array(x)
    if len(x.shape) == 1:
        x = x.reshape(-1, 1)
    y = np.array(y)
    if len(y.shape) == 1:
        y = y.reshape(-1, 1)

    r, c = len(x), len(y)

    D = np.zeros((r + 1, c + 1))
    D[0, 1:] = np.inf
    D[1:, 0] = np.inf

    for i in range(r):
        for j in range(c):
            D[i+1, j+1] = dist(x[i], y[j])

    for i in range(r):
        for j in range(c):
            D[i+1, j+1] += min(D[i, j], D[i, j+1], D[i+1, j])

    D = D[1:, 1:]

    dist = D[-1, -1] / sum(D.shape)

    return dist, D, _trackeback(D)


