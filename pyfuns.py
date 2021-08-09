import numpy as np
from random import randint


def pdens(x, m, s):

    # PDENS Computes the probaaility density values
    # P=PDENS(X,M,S) computes the density value P for
    # X for a gaussian density function with
    # mean value M og standard deviation S.

    p = 1 / (np.sqrt(2 * np.pi) * s) * \
        np.exp(-1 / 2 * np.square((x - m)) / (2 * np.square(s)))

    return p


def pdens2(x, m, s):

    # PDENS Computes the probaaility density values
    # P=PDENS(X,M,S) computes the density value P for
    # X for a gaussian density function with
    # mean value M og standard deviation S.

    N = np.shape(x)[0]
    p = np.zeros(np.shape(x))
    for n in np.arange(0, N - 1):
        p[n] = 1 / (np.sqrt(2 * np.pi) * s) * \
            np.exp(-1 / 2 * np.square((x[n] - m)) / (2 * np.square(s)))

    return p


def absolute(x):
    # ABSOLUTE Computes the absolute value
    # Y=ABSOLUTE(X) computes the absolute value, Y, of X

    if x < 0:
        y = -x
    else:
        y = x

    return y


def divideby2(n):
    # DIVIDEBY2 Divide by 2 as long as the remainder is zero
    # Q=DIVIDEBY2(N) computes the quotienafter maximum number

    q = n
    while np.remainder(q, 2) == 0:
        q = np.fix(q / 2)

    return q

def oddoreven(n):
    # ODDOREVEN Determine if a number is odd or even
    # R = ODDOREVEN(N) returns 1 if N is odd, 0 otherwise.

    r = np.remainder(n,2)
    return r


def oddevensplit(n):
    # ODDOREVENSPLIT Split vector into two with odd and
    # even numbers
    # Y1,Y2 = ODDOREVENSPLIT(N) returns Y1 with odd and Y2
    # Y2 with even numbers
    y1 = []
    y2 = []
    x=[randint(0,9) for p in range(0,n)]
    print(x)
    for i in range(0,n):
        if oddoreven(x[i]):
            #print(str(x[i])+' odd')
            y1.append(x[i])
        else:
            #print(str(x[i])+' even')
            y2.append(x[i])

    return y1,y2
