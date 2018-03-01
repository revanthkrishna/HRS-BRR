# this corresponds to image graph2

from Node import Node
from Path import Path

a = Node('m1')
b = Node('m2')
c = Node('m3')
d = Node('m4')
e = Node('m5')
f = Node('m6')
g = Node('m7')

brown = Path(a, 'brown')
green = Path(e, 'green')
pink = Path(b, 'pink')

a.oet[b] = [brown]

b.iet[a] = [brown]
b.iet[e] = [green]
b.oet[c] = [brown, pink]
b.oet[d] = [green]

c.iet[b] = [brown, pink]
c.iet[f] = [green]
c.oet[d] = [brown, pink]

d.iet[b] = [green]
d.iet[c] = [brown, pink]
d.oet[e] = [brown, pink]
d.oet[f] = [green]

e.iet[d] = [brown, pink]
e.oet[b] = [green]
e.oet[f] = [brown]

f.iet[d] = [green]
f.iet[e] = [brown]
f.oet[c] = [green]
f.oet[g] = [brown]

g.iet[f] = [brown]
