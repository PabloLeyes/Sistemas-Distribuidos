namespace py SDEntrega1Pablo

typedef i32 int

struct Vertex{
    1:int name,
    2:int color,
    3:string description,
    4:double weight
}

struct Edge{
    1:int id,
    2:Vertex origem_vertex,
    3:Vertex destination_vertex,
    4:double weight,
    5:bool Unidirectional,
    6:string description
}

exception OperationFailed { 
    1: string reason
}

exception ObjectNotFound {
    1: string reason
}

exception InvalidObject {
    1:string reason
}


service Services_Vertex_Edge{
    void load_file()
    void save_file()
    
    void createVert(1: int name, 2: int color, 3: string description, 4: double weight) throws (1: OperationFailed operationFailed, 2: InvalidObject invalidObject)
    Vertex readVert(1: int name) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound)
    Vertex updateVert(1: int name, 2: int color, 3: string description, 4: double weight) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound, 3: InvalidObject invalidObject)
    void deletaVert(1: int name) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound, 3: InvalidObject invalidObject)
    list<int> listNeighbours(1: int name) throws (1: OperationFailed operationFailed, 2: InvalidObject invalidObject)
    list<Vertex> listVertexesFromEdge(1: int name) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound)
    list<Edge> listEdgesFromVertex(1: int name) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound)

    Edge createEdge(1: int id, 2: int origem_vertex, 3: int destination_vertex, 4: double weight, 5: bool Unidirectional, 6: string description) throws (1: OperationFailed operationFailed, 2: InvalidObject invalidObject)
    Edge readEdge(1: int id) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound)
    Edge updateEdge(1: int id, 2: int origem_vertex, 3: int destination_vertex, 4: double weight, 5: bool Unidirectional, 6: string description) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound, 3: InvalidObject invalidObject)
    void deletaEdge(1: int id) throws (1: OperationFailed operationFailed, 2: ObjectNotFound objectNotFound, 3: InvalidObject invalidObject)
}