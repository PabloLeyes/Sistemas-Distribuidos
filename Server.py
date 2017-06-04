import sys

sys.path.append('gen-py')

from SDEntrega1Pablo import *
from SDEntrega1Pablo.ttypes import *
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.server import TServer
from thrift.transport import TTransport
import socket
import logging
from threading import Lock


class ServerHandler(object):
    def __init__(self):
        self.List_Vertex = []
        self.List_edges = []
        self.mutex = Lock()
        self.count = 0


    ########### BASIC OPERATIONS ###########

    def check_vertex(self, name):
        for Vertex in self.List_Vertex:
            if (Vertex.name == name):
                raise(OperationFailed("Vertex already exist"))


    def check_edge(self, id):
        for edge in self.List_edges:
            if (edge.id == id):
                raise(OperationFailed("Edge already exist"))


    def load_file(self):
        self.mutex.acquire()

        vertexes_data = open("List_Vertex.txt", 'r').read().splitlines()
        for line in vertexes_data:
            vertex_array = line.split(",")
            newVertex = Vertex(int(vertex_array[0]), int(vertex_array[1]), str(vertex_array[2]), float(vertex_array[3]))
            self.List_Vertex.append(newVertex)


        edges_data = open("List_edges.txt", 'r').read().splitlines()
        for line in edges_data:
            edge_array = line.split(",")
            newEdge = Edge(int(edge_array[0]), int(edge_array[1]), int(edge_array[2]), float(edge_array[3]), bool(edge_array[4]), str(edge_array[5]))
            self.List_edges.append(newEdge)

        self.mutex.release()
        # print self.List_Vertex
        print self.List_edges
        print("Terminei de ler")


    def save_file(self):
        self.mutex.acquire()
        with open("List_Vertex.txt", "w") as file:
            for vert in self.List_Vertex:
                array_of_vertex_value = [vert.name, vert.color, vert.description, vert.weight]
                string_vert = ','.join([str(value) for value in array_of_vertex_value])
                final_string_vert = string_vert + "\n"
                file.write(final_string_vert)

        with open("List_edges.txt", "w") as file:
            for edge in self.List_edges:
                array_of_edge_values = [edge.id, edge.origem_vertex, edge.destination_vertex, edge.weight, edge.Unidirectional, edge.description]
                string_edge = ','.join([str(value) for value in array_of_edge_values])
                final_string_edge = string_edge + "\n"
                file.write(final_string_edge)

        self.mutex.release()
        print("Terminei de Salvar")


    ########### VERTEX OPERATIONS ###########

    def createVert(self, vName, vColor, vDesc, vWeight):
        self.check_vertex(vName)
        newV = Vertex(name=vName, color=vColor, description=vDesc, weight=vWeight)
        self.List_Vertex.append(newV)



    def updateVert(self, name, color, description, weight):
        data = None
        for Vertex in file:
            if (Vertex.name == name):
                Vertex.color = color
                Vertex.description = description
                Vertex.weight = weight
                data = Vertex
        if data == None:
            raise(InvalidObject("Vertex doesn't exist"))
        else:
            data = Vertex.name
            return data          


    def readVert(self, name):
        data = None
        for vertex in self.List_Vertex:
            if vertex.name == name:
                data = vertex
        if data == None:
            raise(InvalidObject("Vertex doesn't exist"))
        else:
            return data


    def deletaVert(self, name):
        data = None
        for vertex in self.List_Vertex:
            if (vertex.name == name):
                data = vertex
                self.List_Vertex.remove(vertex)
        for edge in self.List_edges:
            if (edge.origem_vertex == name or edge.destination_vertex == name ):
                self.List_edges.remove(edge)
        if (data == None):
            raise (OperationFailed("Vertex can't be deleted because it doesn't exist"))
    
    ########### EDGE OPERATIONS ###########
    def createEdge(self, eId, eOrigem_vertex, eDestination_vertex,  eWeight,  eUnidirectional,  eDescription):
        self.check_edge(id)
        newE = Edge(id=eId, origem_vertex=eOrigem_vertex, destination_vertex=eDestination_vertex, weight=eWeight, unidirectional=eUnidirectional, description=eDescription)
        self.List_edge.append(newE)


    def readEdge(self, id):
        data = None
        for edge in self.List_edges:
            if(edge.id == id):
                data = edge
        if data == None:
            raise(InvalidObject("Edge doesn't exist"))
        else:
            return data

    def updateEdge(self, origem_vertex, destination_vertex,  weight,  Unidirectional,  description):
        data = None
        for edge in self.List_edges:
            if(edge.id == id):
                edge.origem_vertex = origem_vertex
                edge.destination_vertex = destination_vertex
                edge.weight = weight
                edge.Unidirectional = Unidirectional
                edge.description = description
                data = edge
        if data == None:
            raise(InvalidObject("Edge doesn't exist"))
        else:
            return data


    def deletaEdge(self, id):
        data = None
        for edge in self.List_edges:
            if (edge.id == id):
                data = edge
                self.List_edge.remove(edge)
        if (data == None):
            raise (OperationFailed("Edge can't be deleted because it doesn't exist"))

    ########### LIST OPERATIONS ###########

    def listEdgesFromVertex(self,vert_name):
        list_edges_from_vert = []
        for edge in self.List_edges:
            if (edge.origem_vertex == vert_name or edge.destination_vertex == vert_name):
                list_edges_from_vert.append(edge)
        return list_edges_from_vert


    def listNeighbours(self, vert_name):
        list_of_neighbours = []
        for edge in List_edges:
            if (edge.origem_vertex == vert_name):
                list_of_neighbours.append(edge.destination_vertex)
            if(edge.destination_vertex == vert_name):
                list_of_neighbours.append(edge.origem_vertex)
        return list_of_neighbours


    def listVertexesFromEdge(self, edge_name):
        list_vertexes_of_edge = []
        for edge in self.List_edges:
            if (edge.name == edge_name):
                list_vertexes_of_edge.append(edge.origem_vertex)
                list_vertexes_of_edge.append(edge.destination_vertex)
        return list_vertexes_of_edge


handler = ServerHandler()

processor = Services_Vertex_Edge.Processor(handler = handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
logging.basicConfig(level=logging.DEBUG)

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print ("Starting python server...")
server.serve()
print ("done!")
