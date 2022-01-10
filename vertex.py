from cs1lib import *
vertex_radius = 10
stroke_width = 5
class Vertex:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        self.adj_list = []

    def __str__(self):
        string = self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: "
        for i in range(len(self.adj_list)):
            string = string + self.adj_list[i].name
            if i < len(self.adj_list) - 1:
                string = string + ", "
        return string

#method to draw a vertex
    def draw_vertex(self,r,g,b):
        set_fill_color(r,g,b)
        disable_stroke()
        draw_circle(self.x,self.y,vertex_radius)

#mathod to draw an edge between the called vertex and a variable vertex
    def draw_edge(self,new_vertex,r,g,b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, vertex_radius)
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(stroke_width)
        draw_line(self.x,self.y,new_vertex.x,new_vertex.y)

#method to draw all edges between a vertex and its adjacent vertices
    def draw_adjacent_edges(self,r,g,b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(stroke_width)
        for x in self.adj_list:
            draw_line(self.x,self.y,x.x,x.y)

#method to determine if the mouse is nearby a vertex
    def mouse_within_nearby(self,x,y):
        if x <= self.x+ vertex_radius + 1 and x >= self.x - vertex_radius -1:
            if y <= self.y+ vertex_radius + 1 and y >= self.y - vertex_radius -1:
                return True