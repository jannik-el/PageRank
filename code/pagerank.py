####################################################
## pagerank.py - version 2
## 14.11.2021
## created by Franek Liszka and Jannik Elsäßer (jels & frli)
## created for Linear Algebra Pagerank Project

import random
import networkx as nx
import numpy as np
import timeit

bigRandom = 'files/bigRandom.txt'
GnutellaFiles = "files/p2p-Gnutella08-mod.txt"
medium = "files/medium.txt"
tiny = "files/tiny.txt"

with open(GnutellaFiles, "rb") as gnutella:
  G = nx.read_adjlist(gnutella, create_using=nx.DiGraph(), nodetype=int)

def random_surfer(G, n, m=0.15):
    """
    The random_surfer function computes the 10 most visited nodes of a network, using the random_surfer simulation.

    Parameters:
    ##############
    G: a Networkx directed network
    n: the amount of iterations for the random surfer to run
    m: the damping factor (default is 0.15)

    Outputs:
    #############
    The 10 most visited nodes in the network
    """

    visited = {i:0 for i in G.nodes()}
    node = random.choice([i for i in G.nodes]) # start node

    for i in range(1, n, 1):
        visited[node] += 1

        if [k for k in G.neighbors(node)] == [] or random.random() <= m:
            node = random.choice([i for i in G.nodes()])

        else:
            node = random.choice([i for i in G.neighbors(node)])

    sorted_list = []
    for w in sorted(visited, key = visited.get):
        sorted_list.append([w, visited[w]])
    

    return sorted_list[-10:][::-1]

def PageRank(G, n, m=0.15):
    """
    The PageRank function computes the 10 most visited nodes of a network, using the Pagerank algorithm.

    Parameters:
    ##############
    G: a Networkx directed network
    n: the amount of iterations for the pagerank algorithm to run
    m: the damping factor (default is 0.15)

    Outputs:
    #############
    The 10 most popular nodes in the network, according to the pagerank algorithm
    """
    size = len(G.nodes())
    G_reverse = G.reverse()

    branching_list = [[i, len(list(G.neighbors(i)))] for i in sorted(G.nodes())]
    branching = np.array(branching_list)

    all_nodes = np.loadtxt(GnutellaFiles, dtype='int')
    dangling = set(i for i in all_nodes[:,1] if i not in all_nodes[:,0])

    rank_vector = {i: 1/size for i in G.nodes()}
    Sxk = m*1/size
    t = 0

    while t < n:

        Dxk = (1-m)*sum(rank_vector[node]/size for node in dangling)

        for node, rank in rank_vector.items():
            backlinks = [i for i in G_reverse.neighbors(node)]
            ranks = [1/len([i for i in G.neighbors(backlink)]) for backlink in backlinks]

            rel_rank = 0 #or A, so the relative rank for a node in the A Matrix

            for i in range(len(backlinks)):
                rel_rank += ranks[i] * rank_vector[int(backlinks[i])]
            rel_rank = (1-m) * rel_rank

            rank_vector[node] = rel_rank + Dxk + Sxk
        t+= 1

    sorted_list = []
    for w in sorted(rank_vector, key = rank_vector.get):
        sorted_list.append([w, rank_vector[w]])

    return sorted_list[-10:][::-1]

def main():
    print("###############################################################################################")
    print("pagerank.py, created by jels and frli for pagerank project in linear algebra and optimization.")
    print("###############################################################################################")

    
    print(random_surfer(G, n=1000, m=0.15)) #ran with 5 million to get reasonable results
    print(PageRank(G, n=50, m=0.15))

if __name__ == "__main__":
    main()




