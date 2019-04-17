import numpy as np
import networkx as nx
import cPickle as cp
import random
import ctypes
import os
import sys
import time
from tqdm import tqdm

sys.path.append( '%s/IMlib' % os.path.dirname(os.path.realpath(__file__)) )
from IMlib import IMLib

#sys.path.append( '%s/../memetracker' % os.path.dirname(os.path.realpath(__file__)) )
#from meme import *
def build_full_graph(pathtofile, graphtype):
    node_dict = {}
    if graphtype == 'undirected':
        g = nx.Graph()
    elif graphtype == 'directed':
        g = nx.DiGraph()
    else:
        print('Unrecognized graph type')
        return -1

    times = []
    with open(pathtofile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    for line in content:
        entries = line.split()
        src_idx = int (entries[0])
        dst_idx = int (entries[1])

        c = 0
        if g.has_edge(src_idx,dst_idx):
                c = g[src_idx][dst_idx]['count']
        g.add_edge(src_idx,dst_idx,weight=0.1,count= 1) 

        times.append(float(entries[-1]))

    return g, node_dict
   
def find_model_file(opt):
    max_n = int(opt['max_n'])
#    min_n = int(opt['min_n'])
    log_file = '%s/log-%d.txt' % (opt['save_dir'],max_n)

    best_r = 0
    best_it = -1
    with open(log_file, 'r') as f:
        for line in f:
            if 'average' in line:
                line = line.split(' ')
                it = int(line[1].strip())
                r = float(line[-1].strip())
                if r > best_r:
                    best_r = r
                    best_it = it
    assert best_it >= 0
    print 'using iter=', best_it, 'with r=', best_r
    return '%s/iter_%d.model' % (opt['save_dir'], best_it)
    
if __name__ == '__main__':
    api = IMLib(sys.argv)
    
    opt = {}
    for i in range(1, len(sys.argv), 2):
        opt[sys.argv[i][1:]] = sys.argv[i + 1]

    g, _ = build_full_graph('%s/DBLP-new.txt' % opt['data_root'],'undirected')

    model_file = find_model_file(opt)
    assert model_file is not None
    print 'loading', model_file
    sys.stdout.flush()
    api.LoadModel(model_file)

    print 'testing'
    sys.stdout.flush()
    api.InsertGraph(g, is_test=True)
    t1 = time.time()
    val, sol = api.GetSol_test(0, nx.number_of_nodes(g))
    t2 = time.time()
    print 'seedset =',
    for i in range(sol[0]):
        print sol[i+1],
    print '\ntime =',t2-t1
