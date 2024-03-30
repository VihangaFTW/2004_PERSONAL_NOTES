from my_queue import CircularQueue
from my_stack import LinkedStack
from my_heap import MinHeap
from math import inf
# adjacency list representation of graphs

class Vertex:
    def __init__(self,id) -> None:
        self.id = id
        # for traversal
        self.discovered = False
        self.visited = False
        self.distance = inf
        self.previous = None
        self.incoming_edges = 0
        self.edges: list[None | Edge] = []
        self.array_index = -1

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
                #* needed for kahn's algorithm
                v2.incoming_edges += 1

    def show_edges(self) -> str:
        all_edges = ""
        for vertex in self.vertices:
            for edge in vertex.edges:
                all_edges += str(edge) + "\n"
        return all_edges
    
    #* Week 4: Kahn's alogorithm topological sort

    def remove_edge(self, u: Vertex, v: Vertex):
        '''
        #! horrible implementation but works
        '''
        # traverse through vertices
        for vertex in self.vertices:
            # first vertex found
            if vertex is u:
                # traverse to find other vertex of edge
                for edge in vertex.edges:
                    # other vertex of edge found so remove the Edge object from start vertex 
                    if edge.v is  v and not edge.directed:
                        #? need to remove the Edge object from end vertex if undirected edge
                        for v_edge in v.edges:
                            if v_edge.u is v:
                                v.edges.remove(v_edge)
                    vertex.edges.remove(edge)
                    return
                
        raise ValueError("Edge does not exist!")
    
    def topological_sort_kahn(self):
        '''
        :prereq: Graph must be a DAG.
        :time: O(V+E) as queue stores every vertex and each edge is visited once
        :space: O(V+E)
        where V is the total number of vertices and E the total number of edges in the graph
        '''
        sorted_vertices = []
    
        # # queue to store all vertices without incoming edges
        to_process = CircularQueue(len(self.vertices))
        starting_vertices = []
        
        for vertex in self.vertices:
            if vertex.incoming_edges == 0:
                starting_vertices.append(vertex)

        # If there are no starting vertices, the graph contains a cycle
        if not starting_vertices:
            raise ValueError("Graph contains a cycle!")
        
        for vertex in starting_vertices:
            to_process.append(vertex)
        
        while to_process:
            current_vertex = to_process.serve()
            sorted_vertices.append(current_vertex.get_id())
            # go thru each outgoing edge of current vertex
            for edge in current_vertex.edges:
                edge.v.incoming_edges -= 1
                if edge.v.incoming_edges == 0:
                    to_process.append(edge.v)
                    
        # # check for cycles
        for vertex in self.vertices:
            if vertex.incoming_edges > 0:
                raise ValueError("Graph contains a cycle!")
        
        # reset incoming edges attribute of all vertices to 0
        self._reset_all_incoming_edges()
        return sorted_vertices

    
    def _reset_all_incoming_edges(self):
        """
        :time comp: O(V) where V is the total number of vertices in the graph.
        :space comp: total and aux is O(1) as we just traverse through self.vertices
        """
        for vertex in self.vertices:
            vertex.incoming_edges = 0

    def _reset_all_distances(self):
        for vertex in self.vertices:
            vertex.distance = inf

    def _reset_all_array_indices(self):
        for vertex in self.vertices:
            vertex.array_index = -1


    def topological_sort_dfs(self):
        stack = LinkedStack()

        for vertex in self.vertices:
            if not vertex.visited:
                self._topological_sort_dfs_aux(vertex,stack)

        sorted_vertices = [None] * len(self.vertices)

        for i in range(len(self.vertices)):
            sorted_vertices[i] = stack.pop().get_id()
        
        return sorted_vertices



    def _topological_sort_dfs_aux(self,u:Vertex, stack: LinkedStack):
        u.visited = True
        for edge in u.edges:
            if edge.v.visited == False:
                self._topological_sort_dfs_aux(edge.v, stack)

        stack.push(u)


    def bfs(self, source: Vertex) -> list[Vertex]:
        source.distance = 0
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
        source.distance = 0
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
        source.distance = 0
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
        source.distance = 0
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
    
    def shortest_distance_dijkstra(self, start_vertex: Vertex, end_vertex: Vertex) -> str:
        '''
        This method calculates the shortest distance between two vertices in the graph using Dijkstra's algorithm which is
        based on a modified BFS with a priority queue (min heap) instead of a queue.
        :prereq: Graph does not have negative edges.
        : start_vertex:- starting vertex of search
        : end_vertex: ending vertex of search.
        : returns a formatted string detailing the shortest distance between the given vertices along with the path to take.
        : time comp:- O((V+E) log V) ???
        : space comp: aux is O(V) as we need to store all the vertices in the heap.
                      total is O(V).
        '''
        # reset instance attributes
        self._reset_all_array_indices()
        self._reset_all_distances()
        
        start_vertex.distance = 0
        discovered = MinHeap(len(self.vertices))
        discovered.add(0,start_vertex)
        while discovered:
            current_vertex = discovered.get_min()[1]
            current_vertex.visited  = True
            if current_vertex == end_vertex:
                break
            for edge in current_vertex.edges:
                vertex = edge.v
                #* the edge can either be a new edge (undiscovered) or an edge that is in the heap (not visited yet)
                if not vertex.discovered:
                    vertex.discovered = True
                    new_distance = current_vertex.distance + edge.w
                    vertex.distance = new_distance
                    vertex.previous = current_vertex
                    discovered.add(new_distance,vertex)
                elif not vertex.visited:
                    updated_distance = current_vertex.distance + edge.w
                    if updated_distance < vertex.distance:
                        vertex.distance = updated_distance
                        vertex.previous = current_vertex
                        discovered.update(vertex,updated_distance)

        shortest_path = []
        shortest_path.append(end_vertex.id)
        prev_vertex = end_vertex.previous
        while prev_vertex:
            shortest_path.append(prev_vertex.id)
            prev_vertex = prev_vertex.previous

        return f'Shortest distance from {start_vertex.id} to {end_vertex.id} is {end_vertex.distance}\
            \nPath taken: {shortest_path[::-1]}' #? #@%* space comp


    def __str__(self):
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex: " + str(vertex) + "\n"
        return return_string


if __name__ == "__main__":
    # v1 = Vertex("FIT1045")
    # v2 = Vertex("MAT1830")
    # v3 = Vertex("FIT1008")
    # v4 = Vertex("FIT2014")
    # v5 = Vertex("FIT2099")
    # v6 = Vertex("FIT2004")
    # v7 = Vertex("FIT3155")
    # v8 = Vertex("FYP")
    # my_graph = Graph([v1,v2,v3,v4,v5,v6,v7,v8])
    # my_graph.add_directed_edge(v1,v3)
    # my_graph.add_directed_edge(v2,v3)
    # my_graph.add_directed_edge(v3,v6)
    # my_graph.add_directed_edge(v3,v5)
    # my_graph.add_directed_edge(v3,v4)
    # my_graph.add_directed_edge(v6,v7)
    # my_graph.add_directed_edge(v7,v8)
    # my_graph.add_undirected_edge(v2,v4)
    # my_graph.add_undirected_edge(v2,v5)
    # my_graph.add_undirected_edge(v3,v6)
    # my_graph.add_undirected_edge(v3,v7)
    # my_graph.add_directed_edge(v6,v8)
    # my_graph.add_undirected_edge(v8,v7)
    #print(my_graph.dfs(v1))
    #print(my_graph.dfs_recur(v1))
    #print(my_graph.shortest_distance_bfs(v1,v4))

    # #* test removing edges
    # my_graph.remove_edge(v1,v2)
    # print(my_graph.show_edges())

    #* testing kahn sort
    #print(my_graph.topological_sort_kahn())
    # print("==========dfs topological sort============")
    # print(my_graph.topological_sort_dfs())


    #* testing dijkstra
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v4 = Vertex("D")
    v5 = Vertex("E")
    graph2 = Graph([v1,v2,v3,v4,v5])
    # add edges
    graph2.add_directed_edge(v1,v3,5)
    graph2.add_directed_edge(v1,v2,10)
    graph2.add_directed_edge(v3,v2,3)
    graph2.add_directed_edge(v3,v4,9)
    graph2.add_directed_edge(v3,v5,2)
    graph2.add_directed_edge(v1,v3,5)
    graph2.add_directed_edge(v2,v3,2)
    graph2.add_directed_edge(v4,v5,4)
    graph2.add_directed_edge(v5,v4,6)
    graph2.add_directed_edge(v2,v4,1)
    print(graph2.shortest_distance_dijkstra(v1,v2))
    

