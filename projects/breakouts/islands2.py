# Write a function that takes a 2D binary array and returns 
# the number of 1 islands. An island consists of 1s that are 
# connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4
# islands consist of - connected components
# connected - neighbors (edges)
# directions, nsew (edges)
# 2d array - graph, more or less?
# returns (shape of solution) -  number of islands
# How could we write a get neighbor function that uses this shape?
# Offset coordinates
# How can find the extent of an island?
# Either of our travels to find all of the nodes in an island
# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1

'''
island #1
ab
ba
b

island #2
ad
bd
be

island #3
c
dc

island #4
da
ea
eb
'''

# Instructor Brian Doyle's Shared Solution
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    return neighbors


def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        v = s.pop()
        if not visited[v[1]][v[0]]:
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dfs(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count

def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))


matrix = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
print_matrix(matrix)
island_counter(matrix)