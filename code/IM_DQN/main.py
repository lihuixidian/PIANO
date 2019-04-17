import numpy as np
import networkx as nx
import cPickle as cp
import random
import ctypes
import os
import sys
from tqdm import tqdm
import Queue as queue

sys.path.append( '%s/IMlib' % os.path.dirname(os.path.realpath(__file__)) )
from IMlib import IMLib
sample_number=0
def build_full_graph(pathtofile, graphtype):
    node_dict = {}
    if graphtype == 'undirected':
        g = nx.Graph()
    elif graphtype == 'directed':
        g = nx.DiGraph()
    else:
        print('Unrecognized graph type .. aborting!')
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
    
def gen_new_graphs(opt, G):
    print 'generating new training graphs'
    sys.stdout.flush()
    api.ClearTrainGraphs()
    for i in tqdm(range(100)):
        g = Breadth_First_Search(G)
        sys.stdout.flush()
	api.InsertGraph(g, is_test=False)

def Breadth_First_Search(G):
    g = nx.Graph()
    g2 = nx.Graph()
    global sample_number
    for line in open("/home/xmt/DISCO-KDD/code/data/7_DBLP_SRW/"+str(sample_number).zfill(3)+'_dblp_SRW'+'.edgelist'):
        line = line.split()
        g2.add_edge(int(line[0]), int(line[1]), weight = 0.1)

    # make dictionary
    sample_number+=1
    numrealnodes = 0
    node_map = {}
    for node in g2.nodes():
        node_map[node] = numrealnodes
        numrealnodes += 1
    # re-create the largest component with nodes indexed from 0 sequentially
    for edge in g2.edges(data=True):
        src_idx = node_map[edge[0]]
        dst_idx = node_map[edge[1]]
        g.add_edge(src_idx, dst_idx,weight= 0.1)
    return g

if __name__ == '__main__':
    api = IMLib(sys.argv)
    opt = {}
    for i in range(1, len(sys.argv), 2):
        opt[sys.argv[i][1:]] = sys.argv[i + 1]
    
    g_undirected, _ = build_full_graph('%s/DBLP-new.txt' % opt['data_root'],'undirected')
    print(nx.number_of_nodes(g_undirected))
    print(nx.number_of_edges(g_undirected)) #di_graph
    api.InsertGraph(g_undirected, is_test=True)
    # startup
    gen_new_graphs(opt, g_undirected)
    for i in range(10):
        api.lib.PlayGame(100, ctypes.c_double(1.0))
    api.TakeSnapshot()

    eps_start = 1.0
    eps_end = 0.05
    eps_step = 10000.0
    for iter in range(int(opt['max_iter'])):
        if iter and iter % 5000 == 0:
            gen_new_graphs(opt, g_undirected)
        eps = eps_end + max(0., (eps_start - eps_end) * (eps_step - iter) / eps_step)
        if iter % 10 == 0:
            api.lib.PlayGame(10, ctypes.c_double(eps))

        if iter % 300 == 0:
            frac = api.lib.Test(0)
            print 'iter', iter, 'eps', eps, 'average r: ', frac
            sys.stdout.flush()
            model_path = '%s/iter_%d.model' % (opt['save_dir'], iter)
            api.SaveModel(model_path)

        if iter % 1000 == 0:
            api.TakeSnapshot()

        api.lib.Fit()
