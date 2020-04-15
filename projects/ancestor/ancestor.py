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


# BFT
def earliest_ancestor(ancestors, starting_node):
    # Create Graph, add vertices and edges
    g = Graph()

    # Add vertices first, then edges.  Edges won't add until vertices exist.
    cust_add_vert(g, ancestors)
    cust_add_edges(g, ancestors)

    qq = Queue()
    qq.enqueue(starting_node) 

    print("Latest graph: ", g.vertices)
    visited = set()

    while qq.size() > 0:
        path = qq.dequeue()

        if path not in visited:
            # do the thing...
            print("path: ", path)
            # add path[0] to visited
            visited.add(path)
            print("visited: ", visited)
            for key,vals in g.vertices.items():
                print("key: ", key)
                if vals is not None:
                    for val in vals: 
                        print("val: ", val)
    print(g.vertices)
                # new_path = path.copy()
                # print("neighbor: ", neighbor)
                # print("new_path", new_path)
                # new_path.append(neighbor)
                # qq.enqueue(new_path)
    # print("Path: ", path)
    return path
    
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

    # qq = Queue()
    # qq.enqueue(starting_node) 

    # visited = set()
    # print("queue size: ", qq.size())

    # while qq.size() > 0:
    #     path = qq.dequeue()
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
    #             qq.enqueue(new_path)
    # print("Path: ", path)
    # return path

# ****Helper Functions****
# add vert method.
def cust_add_vert(graph, ancestors):
    for tup in ancestors:
        # add_vertex is a Graph class method from graph.py.
        graph.add_vertex(tup[0])
        graph.add_vertex(tup[1])

# add edges method
def cust_add_edges(graph, ancestors):
    for tup in ancestors:
        graph.add_edge(tup[0], tup[1])

# *****END HELPERS******
# pdb.set_trace()


# for testing/checking code.
parent_child_rel = [(10, 1), (1,3), (2,3), (4,5), (4,8), (3,6), (5,6), (5,7), (11,8), (8,9)]

# def test_func(arr, starting_node=6):
#     path = [] #(3,6), (5,6)
#     starting_node = starting_node
#     for el in arr:
#         p = el[0]
#         c = el[1]
#         if c is starting_node:
#             path.append(el)
#             test_func(path, )


earliest_ancestor(parent_child_rel, 6)
# qq = Queue()
# ss = Stack()
# print("ancestors: ", parent_child_rel)
# print(parent_child_rel[0])
# print("first element of last tuple in parent_child_rel array/graph: ", parent_child_rel[-1][0])
# print(qq.size())
# print(ss.size())