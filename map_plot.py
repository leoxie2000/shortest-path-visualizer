
from vertex import Vertex
from load_graph import *
from cs1lib import *
from bfs import *


x = load_image("dartmouth_map.png")
vertex_dict = load_graph("dartmouth_graph.txt")


start_vertex = None
goal_vertex = None

#track the movement of the mouse when there's a start vertex
def mmoved(mx,my):
    global start_vertex, goal_vertex
    if start_vertex != None:
        for i in vertex_dict:
            if vertex_dict[i].mouse_within_nearby(mx, my):
                goal_vertex = vertex_dict[i]

#when mouse is pressed near a vertex, pick that as the start
def mpressed(mx,my):
    global start_vertex
    for i in vertex_dict:
        if vertex_dict[i].mouse_within_nearby(mx,my):
            start_vertex = vertex_dict[i]

#main draw function that draws the path according to breadth-first search, starting and goal vertex
def draw():
    global x,start_vertex,goal_vertex
    draw_image(x,0,0)

    for i in vertex_dict:
        vertex_dict[i].draw_vertex(0,0,1)
        vertex_dict[i].draw_adjacent_edges(0,0,1)
    if start_vertex != None:
        start_vertex.draw_vertex(1,0,0)
        if goal_vertex != None:
            goal_vertex.draw_vertex(1,0,0)
            path = bfs(start_vertex,goal_vertex)
            for i in range(len(path) - 1):
                path[i].draw_edge(path[i+1],1,0,0)




start_graphics(draw,width=1012,height=811, mouse_press = mpressed,mouse_move=mmoved)