from Map import Component
from Map import Map
from Map import Pin
import Router
import time

cs = []
first = Component((12, 18), (10, 16))
second = Component((12, 18), (33, 16))
third = Component((12, 18), (56, 16))
cs.append(first)
cs.append(second)
cs.append(third)
nets = []

net1 =[Pin('N$1', (15,15)), Pin('N$1',(37, 15)), Pin('N$1',(62,34))]
net2 =[Pin('N$2', (15,34)), Pin('N$2',(37, 34)), Pin('N$2',(62,15))]
nets.append(net1)
nets.append(net2)
map1 = Map(80, 50, cs, nets)

Router.route(map1, "router_output.txt")