# -*- coding: utf-8 -
import queue
import random
import networkx as nx
from multiprocessing import Process
import multiprocessing

influence_sum=multiprocessing.Value("i",0)

def process():
    influence = 0
    for i in range(0, 50):
        influence += simulate(set(seedset[:]))
    with influence_sum.get_lock():
        influence_sum.value  += influence
        
def simulate(seedset):
    active = []
    for i in range (0, g.number_of_nodes()):
        active.append(0)
    simul_inf = 0
    q1 = queue.Queue()

    k1 = len(seedset)
    for it in seedset:
        q1.put(it)
        active[it] = 1
        simul_inf += 1
    while q1.qsize() != 0:
        expend = q1.get()
        for neigh in g[expend]:
            randDouble = random.random()
            if randDouble > 0.1:
                continue
            if active[neigh] == 1:
                continue
            if active[neigh] !=1:
                active[neigh] = 1
                q1.put(neigh)
                simul_inf += 1
    return simul_inf

g = nx.Graph()
for line in open("DBLP-new.txt"):
    line = line.split()
    g.add_edge(int(line[0]), int(line[1]), weight = float(line[2]))
seedset="3335 3344 166 14689 13940 30094 864 3297 13841 13810 15325 3325 3345 1826 1832 13952 44 7226 2485 27137 6318 35861 1447 3399 1817 9400 17110 3299 2005 7006 9799 10277 13931 6325 1196 2976 66101 6327 7437 8622 28674 60436 2545 6317 2911 4298 1499 2142 7429 67246"
seedset = seedset.split(' ')
seedset=list(map(int,seedset))
process_list = []
for j in range(20):
    process_list.append(Process(target=process))
    process_list[-1].start()

for p in process_list:
    p.join()

print('influence = '+str(influence_sum.value/1000))
