import sys
sys.path.append('../graph')

from graph import Graph
from util import Queue, Stack

import pdb

'''
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
'''



def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    cust_add_vert(g, ancestors)
    cust_add_edges(g, ancestors)

    print("Latest graph: ", g.vertices)


    qq = Queue()
    qq.enqueue(starting_node) 

    visited = set()

    # while qq.size > 0:
    #     path = qq.dequeue()

    #     if path[0] not in visited:
    #         # do the thing...
    #         # add path[0] to visited
    #         visited.add(path[0])
    #         for neighbor in g.get_neighbors(path[0])


# ****Helper Functions****
# add vert method.
def cust_add_vert(graph, ancestors):
    for tup in ancestors:
        # verts
        graph.add_vertex(tup[0])
        graph.add_vertex(tup[1])

def cust_add_edges(graph, ancestors):
    for tup in ancestors:
        graph.add_edge(tup[0], tup[1])

# *****END HELPERS******
# pdb.set_trace()


# for testing/checking code.
parent_child_rel = [(10, 1), (1,3), (2,3), (4,5), (4,8), (3,6), (5,6), (5,7), (11,8), (8,9)]
earliest_ancestor(parent_child_rel, 6)
qq = Queue()
ss = Stack()
print(parent_child_rel)
print(parent_child_rel[0])
print("first element of last tuple in parent_child_rel array/graph: ", parent_child_rel[-1][0])
# print(qq.size)
# print(ss.size)