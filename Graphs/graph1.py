# this corresponds to image graph1

from Node import Node
from Path import Path

a = Node('m1')
b = Node('m2')
c = Node('m3')
d = Node('m4')
e = Node('m5')
f = Node('m6')
g = Node('m7')
x = Node('m8')

p1 = Path(a, 'p1')
p2 = Path(g, 'p2')
p3 = Path(e, 'p3')

up = Path(x, 'up')

a.oet[b] = [p1]

b.oet[c] = [p1, p2, up]
b.iet[g] = [p2]
b.iet[x] = [up]
b.iet[a] = [p1]

c.oet[d] = [p1]
c.oet[e] = [p2]
c.iet[b] = [p1, p2, up]

d.iet[c] = [p1]

e.oet[f] = [p2, p3]
e.iet[c] = [p2]

f.iet[e] = [p2, p3]

g.oet[b] = [p2]

x.oet[b] = [up]

