import sys
import numpy as np

with sys.stdin as F:
    lines = F.readlines()
    i = 1
    CASE = 1
    while (i < len(lines)):
        COLBAD = 0
        LINBAD = 0
        N = int(lines[i].rstrip('\n'))
        mat = np.zeros((N, N))
        i += 1
        k = 0
        while i < i + N:
            j = 0
            tab = lines[i].rstrip('\n').split(' ')
            for j in range(N):
                mat[k, j] = tab[j]
            k = k + 1
            i = i + 1
        trace = 0
        for j in range(N):
            trace += mat[j, j]

        for j in range(N):
            H_COL = {}
            H_LIN = {}
            for k in range(N):
                H_COL[mat[j, k]] = 1
                H_COL[mat[k, j]] = 1
            if len(H_COL.keys()) != N:
                COLBAD += 1
            if len(H_LIN.keys()) != N:
                LINBAD += 1
        print('Case #%d: %d %d %d' % (CASE, trace, LINBAD, COLBAD))
        CASE += 1