import time
import pdb
import sys
sys.path.append('../graph')

from graph import Graph
from util import Queue, Stack


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
        # print("starting vert value is 0: ", -1)
        return -1

    # return results from dft
    # return cust_dft(g, starting_node)  
    
    # return results from bft
    return cust_bft(g, starting_node)    



# ****Helper Functions****
# add vert method.
def build_graph(graph, ancestors):
    for tup in ancestors:
        # add_vertex is a Graph class method from graph.py.
        graph.add_vertex(tup[0])
        graph.add_vertex(tup[1])
        # invert the edges to make a top to bottom graph.
        graph.add_edge(tup[1], tup[0])

# depth first traversal for earliest ancestor.
def cust_dft(graph, starting_node):
    # start_time = time.time()
    # create Stack.
    ss = Stack()
    ss.push([starting_node]) 

    # print("Latest graph: ", graph.vertices)
    visited = set()

    # tracking ancestors path
    anc_path = [starting_node]


    while ss.size() > 0:
        path = ss.pop()

        # do the thing
        if len(path) > len(anc_path):
            anc_path = path

        if len(path) == len(anc_path):
            if path[-1] < anc_path[-1]:
                anc_path = path

        # check if vert/node has been visited
        if path[-1] not in visited:
            # print("path: ", path[-1])
            # add path[-1] to visited
            visited.add(path[-1])

            for neighbor in graph.get_neighbors(path[-1]):
                # make copy of path from Stack
                new_path = path.copy()
                # adds next value/vert to the copied path
                new_path.append(neighbor)
                # add/push the latest path to the Stack
                ss.push(new_path)
    # end_time = time.time()
    # print("DFT: ", (end_time - start_time) * 1000)    
    return anc_path[-1]

# bft approach
def cust_bft(graph, starting_vert):
    # start_time = time.time()

    qq = Queue()
    qq.enqueue([starting_vert])

    visited = set()
    anc_path = [starting_vert]

    while qq.size() > 0:
        path = qq.dequeue()
        # print("dequeue path: ", path)

        if len(path) > len(anc_path):
            anc_path = path
        
        if len(path) == len(anc_path):
            if path[-1] < anc_path[-1]:
                anc_path = path

        if path[-1] not in visited:
            visited.add(path[-1])

            for next_vert in graph.get_neighbors(path[-1]):
                path_copy = list(path)
                path_copy.append(next_vert)
                qq.enqueue(path_copy)
            
    # end_time = time.time()
    # print("BFT: ", (end_time - start_time) * 1000)  
    return anc_path[-1]


# *****END HELPERS******
# **python debugger**
# pdb.set_trace()

# Theodore Ngo's Without creating/using Graph Class Recursive implementation:
def teddy_ngo_earliest_ancestor(ancestors, starting_node, visited=None):
    if visited is None:
        visited = []
    
    for a in ancestors:
        if a[1] == starting_node:
            visited.append(a[0])
            return teddy_ngo_earliest_ancestor(ancestors, a[0, visited])
        if a[0] == starting_node and a[0] in visited:
            return a[0]
    return -1


# for testing/checking code.
parent_child_rel = [(10, 1), (1,3), (2,3), (4,5), (4,8), (3,6), (5,6), (5,7), (11,8), (8,9)]


earliest_ancestor(parent_child_rel, 8)
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




