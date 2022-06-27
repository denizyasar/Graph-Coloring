from asyncore import write
from os.path import exists
from typing import List

# vertex class


class Vertex:

    def __init__(self, id):
        self.id = id
        self.neighbourList: list[Vertex] = []
        self.color = -1

    # add neighbour to list by checking id

    def addNeighbour(self, vertex):
        for v in self.neighbourList:
            if v.id == vertex.id:
                break
        else:
            self.neighbourList.append(vertex)


def processFile(fileName):
    # read file
    with open(fileName, 'r') as file:
        # check first line for vertex count, add list
        first_line = file.readline()
        firstline = first_line.split()
        vertex_count = int(firstline[1])
        for i in range(vertex_count+1):
            vertices.append(Vertex(i))
        # add vertices to neighbours list
        lines = file.readlines()
        for line in lines:
            line = line.split()
            val1 = int(line[1])
            val2 = int(line[2])
            vertices[val2].addNeighbour(vertices[val1])
            vertices[val1].addNeighbour(vertices[val2])


def processColoring():
    # start from 1st vertex
    vertices[1].color = 0
    for vertex in vertices[1:]:
        color = 0
        # for every vertex in neighbour list
        for neighbour in vertex.neighbourList:
            # check if color exist
            if neighbour.color == -1:
                # check if color is equal to mother vertex
                if vertex.color == color:
                    color += 1
                neighbour.color = color
                color += 1


vertices: list[Vertex] = []


def main():
    fileName = input("Enter source text:")

    if not exists(fileName):
        print("File does not exist !")
        return

    processFile(fileName)  # read file
    processColoring()  # do coloring
    # find max color number
    color_count = 0
    for vertex in vertices[1:]:
        if vertex.color > color_count:
            color_count = vertex.color
    with open("output.txt", 'w') as file:
        # write color count adding 1 (0 value)
        file.write(str(color_count+1)+"\n")
        # write vertex colors in list
        for vertex in vertices[1:]:
            file.write(str(vertex.color) + " ")


if __name__ == "__main__":
    main()
