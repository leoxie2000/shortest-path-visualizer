from vertex import Vertex
def load_graph(filename):
    open_file = open("dartmouth_graph.txt","r")

#making vertext for every object in the file and adding them to the dictionary
    vertex_dict = {}
    for bigline in open_file:
        bigline = bigline.strip().split(";")
        vertex_name = bigline[0]
        location = bigline[2].split(", ")

        v1 = Vertex(vertex_name,int(location[0]),int(location[1]))
        vertex_dict[vertex_name] = v1
    open_file.close()

#making the adjacent list of the vertices
    open2 = open("dartmouth_graph.txt","r")
    for bigline in open2:
        bigline = bigline.strip().split(";")
        vertex_name = bigline[0]
        adjacent = bigline[1].strip().split(", ")
        for object in adjacent:
            vertex_dict[vertex_name].adj_list.append(vertex_dict[object])


    return vertex_dict
    open2.close()
load_graph("dartmouth_graph.txt")
