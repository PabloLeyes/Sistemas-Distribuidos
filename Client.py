
import sys
sys.path.append('gen-py/')

import socket

from SDEntrega1Pablo import Services_Vertex_Edge
from SDEntrega1Pablo.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

port = 9090




transport = TSocket.TSocket('localhost', port)

transport = TTransport.TBufferedTransport(transport)

protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Services_Vertex_Edge.Client(protocol)

conexao = True

transport.open()
print("Loading File")
client.load_file()
print("Creating Vertex")
# client.createVert(1,1,"t1",1.1)
client.createVert(9,2,"t1",1.1)
# client.readVert()
# client.updateVert()
# client.deletaVert(9) 
# client.createEdge()
# client.readEdge()
# client.updateEdge()
# client.deletaEdge()
# print(client.listEdges())
# print(client.listVertexes())
# print(client.listVizinhos())

print("Saving Changes")
client.save_file()



print ("Loging off")
transport.close()

