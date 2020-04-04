import sys
import numpy as np

with sys.stdin as F:

    lines = F.readlines()

    CATOT = int(lines[0].rstrip('\n'))
    lines = lines[1:]
    index = 0
    case = 1

    while index < len(lines):
        if case>CATOT:
            print(lines[index].rstrip('\n'))
            index = index+1
        else:
            N = int(lines[index].rstrip('\n'))
            index = index+1
            index_end = index + N
            taches = []
            fins = []
            while index < index_end:
                tab = lines[index].rstrip('\n').split(' ')
                taches.append((int(tab[0]), int(tab[1])))
                fins.append(int(tab[1]))
                index = index+1

            C = np.zeros(24*60).astype('bool')
            J = np.zeros(24*60).astype('bool')
            assignements = np.zeros(len(taches))
            ordre = np.argsort(fins)
            impossible = False
            for i in range(len(taches)):
                (debut, fin) = taches[ordre[i]]
                if np.max(C[debut:fin]) == 0:
                    C[debut:fin] = 1
                    assignements[ordre[i]] = 1
                else:
                    if np.max(J[debut:fin]) == 0:
                        J[debut:fin] = 1
                        assignements[ordre[i]] = 0
                    else:
                        impossible = True
                        break
            s = 'IMPOSSIBLE'
            if not impossible:
                s = ''
                for i in range(len(taches)):
                    if assignements[i] == 1:
                        s += 'C'
                    else:
                        s += 'J'

            print('Case #%d: %s' %(case, s))
            case += 1