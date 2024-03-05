from my_queue import CircularQueue
from my_stack import LinkedStack
# adjacency list representation of graphs

class Vertex:
    def __init__(self,id) -> None:
        self.id = id
        # for traversal
        self.discovered = False
        self.visited = False
        self.distance = 0 
        self.previous = None
        self.edges: list[None | Edge] = []

    def added_to_queue(self) -> None:
        self.discovered =  True

    def visit_node(self) -> None:
        self.visited = True

    def get_id(self):
        return self.id
    
    def __str__(self)-> str:
        return str(self.id)


class Edge:
    def __init__(self,u,v,w, directed=False):
        #* u is the start vertex, v is the end vertex, w is the weight
        self.u: Vertex = u
        self.v: Vertex = v
        self.w: int|None = w
        self.directed = directed

    def __str__(self):
        if self.directed:
            return f"Vertex {self.u} ---> Vertex {self.v}  Weight = {self.w}"
        else:
            return f"Vertex {self.u} --- Vertex {self.v}  Weight = {self.w}"


class Graph:
    '''
    This is a class for a Graph object. Each Graph object contains a list of Vertex objects.
    Each Vertex object contains a list of adjacent Edge objects.
    Each Edge object stores the starting and ending Vertex object and the weight of the edge if it exists.
    '''
    
    def __init__(self, vertices: list[Vertex]) -> None:
        # vertices array 
        self.vertices: list = [None] * len(vertices)
        for i in range(len(vertices)):
            self.vertices[i] = vertices[i]

        '''
        # adjacency matrix implementation
        self.matrix = [None] * len(vertices)
        for i in range(len(vertices)):
            self.matrix[i] = [None] * len(vertices)
        '''
    
    def add_vertex(self,vertex: Vertex) -> None:
        self.vertices.append(vertex)
    
    def add_undirected_edge(self, v1: Vertex, v2: Vertex, weight=None) -> None:
        for vertex in self.vertices:
            if vertex.get_id() ==  v1.get_id():
                vertex.edges.append(Edge(v1,v2,weight))
            if vertex.get_id() ==  v2.get_id():
                vertex.edges.append(Edge(v2,v1,weight))


    def add_directed_edge(self, v1: Vertex, v2: Vertex, weight=None) -> None:
        for vertex in self.vertices:
            if vertex.get_id() ==  v1.get_id():
                vertex.edges.append(Edge(v1,v2,weight,True))

    def show_edges(self) -> str:
        all_edges = ""
        for vertex in self.vertices:
            for edge in vertex.edges:
                all_edges += str(edge) + "\n"
        return all_edges


    def bfs(self, source: Vertex) -> list[Vertex]:
        # queue for discovered vertices
        discovered = CircularQueue(len(self.vertices))
        visited = []
        # we discovered the soruce since we start from this vertex, otherwise this vertex will repeat
        source.discovered = True
        discovered.append(source)
        
        # loop until queue is empty (until all vertices discovered)
        while discovered:
            current_vertex = discovered.serve()
            current_vertex.visited = True
            visited.append(current_vertex.id)
            # add the adjacent vertices of the current vertex to queue
            for edge in current_vertex.edges:
                if not edge.v.discovered:
                    discovered.append(edge.v)
                    edge.v.discovered = True
        return visited
    

    def dfs(self, source: Vertex) -> list:
        # queue for discovered vertices
        discovered = LinkedStack(len(self.vertices))
        visited = []
        # we discovered the soruce since we start from this vertex, otherwise this vertex will repeat
        source.discovered = True
        discovered.push(source)
        
        # loop until stack is empty (until all vertices discovered)
        while discovered:
            current_vertex = discovered.pop()
            current_vertex.visited = True
            visited.append(current_vertex.id)
            # add the adjacent vertices of the current vertex to stack
            for edge in current_vertex.edges:
                if not edge.v.discovered:
                    discovered.push(edge.v)
                    edge.v.discovered = True
        return visited


#!=================================== Recursive dfs ==========================================
    def dfs_recur(self,source:Vertex) ->list:
        return self._dfs_recur_aux(source,[])
    
    def _dfs_recur_aux(self, current_vertex:Vertex, visited_lst: list) -> list:
        
        if current_vertex.visited:
            return visited_lst
        current_vertex.visited = True
        visited_lst.append(current_vertex.id)
        for edge in current_vertex.edges:
            next_vertex = edge.v      # ignore linting error
            if not next_vertex.visited:
                visited_lst = self._dfs_recur_aux(next_vertex,visited_lst)

        return visited_lst
#!=============================================================================================

    def shortest_distance_bfs(self, source: Vertex, target: Vertex) -> str:
        '''
        This function finds the shortest distance from the source vertex to the target vertex
        in an unweighted graph using bfs. Note that only one of the shortest paths will be returned if
        multiple short paths exist.
        : param source: starting vertex of search
        : param target: the ending vertex of search
        : return: a formatted string with the shortest distance along with possible path taken
        '''
        # queue for discovered vertices
        discovered = CircularQueue(len(self.vertices))
        #set default target vertex to source
        target_distance: tuple[Vertex,int] = (source,0)       
        source.discovered = True
        discovered.append(source)
        
        # loop until queue is empty (until all vertices discovered)
        while discovered:
            current_vertex = discovered.serve()
            current_vertex.visited = True
            if current_vertex == target:
                target_distance = (current_vertex,current_vertex.distance)
                break
            # add the adjacent vertices of the current vertex to queue
            for edge in current_vertex.edges:
                if not edge.v.discovered:
                    edge.v.distance = edge.u.distance + 1
                    edge.v.previous = edge.u
                    discovered.append(edge.v)
                    edge.v.discovered = True
        
        #* backtracking of path from target to source
        backtrack_path = []
        # add target vertex to path first
        backtrack_path.append(target_distance[0].id)
        # extract prev vertex of target
        prev_vertex = target_distance[0].previous 
        while prev_vertex:
            backtrack_path.append(prev_vertex.id)
            prev_vertex = prev_vertex.previous
        
        return f'Shortest distance: {target_distance[1]}\nPath: {backtrack_path[::-1]}'


    def __str__(self):
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex: " + str(vertex) + "\n"
        return return_string


if __name__ == "__main__":
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)
    v7 = Vertex(7)
    v8 = Vertex(8)
    my_graph = Graph([v1,v2,v3,v4,v5,v6,v7])
    my_graph.add_undirected_edge(v1,v2)
    my_graph.add_undirected_edge(v1,v3)
    my_graph.add_undirected_edge(v2,v4)
    my_graph.add_undirected_edge(v2,v5)
    my_graph.add_undirected_edge(v3,v6)
    my_graph.add_undirected_edge(v3,v7)
    my_graph.add_directed_edge(v6,v8)
    my_graph.add_undirected_edge(v8,v7)
    #print(my_graph.dfs(v1))
    #print(my_graph.dfs_recur(v1))
    print(my_graph.shortest_distance_bfs(v1,v4))
