import sys
import numpy as np

with open('par.txt') as F:
    lines = F.readlines()[1:]
    case = 1
    for i in range(len(lines)):
        line = lines[i].rstrip('\n')
        j = 0
        s = ''
        while(j<len(line)):
            if line[j] == '0':
                s = s+'0'
                j = j+1
            elif line[j] == '1':
                s = s+'(1'
                j = j+1
                while(j<len(line) and line[j] == '1'):
                    s = s+'1'
                    j = j+1
                s = s+')'
        print('Case #%d: %s' % (case, s))
        case += 1