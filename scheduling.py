import sys
import numpy as np

with sys.stdin as F:
    lines = F.readlines()[1:]
    index = 0
    case = 1
    while index < len(lines):
        N = int(lines[index].rstrip('\n'))
        index = index+1
        index_end = index + N
        taches = []
        while index < index_end:
            tab = lines[index].rstrip('\n').split(' ')
            taches.append((int(tab[0]), int(tab[1])))
            index = index+1
        C = np.zeros(24*60)
        J = np.zeros(24*60)
        s = ''
        for i in range(len(taches)):
            (debut, fin) = taches[i]
            if np.sum(C[debut:fin]) == 0:
                C[debut:fin] = 1
                s+='C'
            else:
                if np.sum(J[debut:fin]) == 0:
                    J[debut:fin] = 1
                    s+='J'
                else:
                    s = 'IMPOSSIBLE'
                    break
        print('Case #%d: %s' %(case, s))
        case += 1