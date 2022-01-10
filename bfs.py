from collections import deque
from load_graph import *
from vertex import Vertex

vertex_dict = load_graph("dartmouth_graph.txt")

#function to return the list that lead up to the goal vertex from the startvertex, tracing back
def bfs(start_vertex, goal_vertex):
    backpointer_dict = {}
    start = start_vertex

    d = deque()
    d.append(start)
    backpointer_dict[start] = None
    path = []
    path.append(start)


#only add vertexes when they are not in the dictionary already. Once the goal is reached, trace back to find the path
    while len(d) > 0:
        current_vertex = d.popleft()
        if goal_vertex not in backpointer_dict:
            for x in current_vertex.adj_list:
                if x not in backpointer_dict:
                    backpointer_dict[x] = current_vertex
                    d.append(x)
        elif goal_vertex in backpointer_dict:
            current_vertex = goal_vertex
            while backpointer_dict[current_vertex] != None:
                path.insert(1,current_vertex)
                current_vertex = backpointer_dict[current_vertex]
            return path


