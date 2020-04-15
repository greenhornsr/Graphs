import sys
sys.path.append('../graph')

from graph import Graph
from util import Queue, Stack

import pdb

# Original Graph
'''
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
'''
# Reverse the Graph.?
'''
     6   7   9
    / \ /   / 
   3   5   8
  / \   \ / \
 1   2   4  11
  \
  10 
'''


# DFT
def earliest_ancestor(ancestors, starting_node):
    # Create Graph, add vertices and edges
    g = Graph()

    # Add vertices first, then edges.  Edges won't add until vertices exist.
    build_graph(g, ancestors)

    # if length of the value in any given vert is 0(empty), return negative 1.
    if len(g.vertices[starting_node]) is 0:
        # print("test")
        return -1

    return cust_dft(g, starting_node)    



# ****Helper Functions****
# add vert method.
def build_graph(graph, ancestors):
    for tup in ancestors:
        # add_vertex is a Graph class method from graph.py.
        graph.add_vertex(tup[0])
        graph.add_vertex(tup[1])
        # invert the edges to make a top to bottom graph.
        graph.add_edge(tup[1], tup[0])

def cust_dft(g, starting_node):
    # create Stack.
    ss = Stack()
    ss.push([starting_node]) 

    print("Latest graph: ", g.vertices)
    visited = set()

    # tracking ancestors path
    anc_path = [starting_node]


    while ss.size() > 0:
        path = ss.pop()

        if len(path) > len(anc_path):
            anc_path = path

        if len(path) == len(anc_path):
            if path[-1] < anc_path[-1]:
                anc_path = path


        if path[-1] not in visited:
            # do the thing...
            # print("path: ", path[-1])
            # add path[-1] to visited
            visited.add(path[-1])
                        
            for neighbor in g.get_neighbors(path[-1]):
                new_path = path.copy()
                # print("new_path", new_path)
                new_path.append(neighbor)
                ss.push(new_path)
        
    return anc_path[-1]



# *****END HELPERS******
# pdb.set_trace()

# for testing/checking code.
parent_child_rel = [(10, 1), (1,3), (2,3), (4,5), (4,8), (3,6), (5,6), (5,7), (11,8), (8,9)]



earliest_ancestor(parent_child_rel, 6)
# qq = Queue()
# ss = Stack()
# print("ancestors: ", parent_child_rel)
# print(parent_child_rel[0])
# print("first element of last tuple in parent_child_rel array/graph: ", parent_child_rel[-1][0])
# print(qq.size())
# print(ss.size())




# MY EFFORTS TO GET THERE....
            # for k,v in g.vertices.items():
            #     # print(g.vertices[starting_node])
            #     print("key:", k, "v: ", v)
            #     for val in v:
            #         print("val: ", val)
            #         if val is starting_node:
            #             visited.add(k)
            #             print("new visited", visited)
            #             print("path is same as val!: ", path)


    
    # return("result: ", result)

    # ss = Stack()
    # ss.push(starting_node) 

    # visited = set()
    # print("stack size: ", ss.size())

    # while ss.size() > 0:
    #     path = ss.pop()
    #     # print("path: ", path)

    #     if path not in visited:
    #         # do the thing...
    #         print("path: ", path)
    #         # add path[0] to visited
    #         visited.add(path)
    #         print("visited: ", visited)
    #         for neighbor in g.get_neighbors(path):
    #             new_path = path.copy()
    #             print("new_path", new_path)
    #             new_path.append(neighbor)
    #             ss.push(new_path)
    # print("Path: ", path)
    # return path




