import numpy as np


def findpeaks(y):
    # FINDPEAKS  Find peaks in real vector.
    #       ind = findpeaks(y) finds the indices (ind) which are
    #       local maxima in the sequence y.
    #
    #       [ind,peaks] = findpeaks(y) returns the value of the peaks at
    #       these locations, i.e. peaks=y(ind);
    #
    #       Funksjonen ble funnet i Matlab Support av Eli Vatland, våren 1998
    #

    y = y.reshape(y.size, 1)
    N = y.size

    dy = np.diff(y, 1, 0)
    b1 = np.vstack((dy, 0)) < 0
    b2 = np.vstack((0, dy)) >= 0

    ind = np.where(b1 & b2)[0]  # Where returns a tuple
    ind = ind.reshape(ind.size, 1)

    if y[-2] < y[-1]:
        ind = np.vstack((ind, N - 1))

    peaks = y[ind, 0]

    return ind, peaks
