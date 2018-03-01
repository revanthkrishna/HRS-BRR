from function_printSimPaths import printSimPaths
from graph3 import *


def printOet(d):
    for i in d.keys():
        print(i.getMovieID(), ':', end='')
        for j in d[i]:
            print(j.getPathID(), end=' ')
        print(' ')

# printOet(c.oet)


printSimPaths(brown)




    




