import random
import networkx as nx
import numpy as np

bigRandom = 'files/bigRandom.txt'
GnutellaFiles = "files/p2p-Gnutella08-mod.txt"
medium = "files/medium.txt"
tiny = "files/tiny.txt"

with open(GnutellaFiles, "rb") as gnutella:
  G = nx.read_adjlist(gnutella, create_using=nx.DiGraph(), nodetype=int)

def random_surfer(G, n, m):
    # create dictionary for nodes and times visited

    visited = {i:0 for i in G.nodes()}
    node = random.choice([i for i in G.nodes]) # start node
    i = 0

    while i <= n:
        visited[node] += 1

        if [k for k in G.neighbors(node)] == [] or random.random() <= m:
            node = random.choice([i for i in G.nodes()])

        else:
            node = random.choice([i for i in G.neighbors(node)])
        i+=1

    sorted_list = []
    for w in sorted(visited, key = visited.get):
        sorted_list.append([w, visited[w]])

    return sorted_list[-20:]
    
n = 1000000
m = 0.15
print(random_surfer(G, n, m))