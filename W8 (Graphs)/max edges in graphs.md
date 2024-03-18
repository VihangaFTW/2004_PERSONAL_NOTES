In a simple directed graph, each edge has an orientation, meaning it goes from one vertex to another, but not the other way around. So, for a graph with V vertices, each vertex can have an edge to V-1 other vertices (not counting itself). Therefore, the maximum number of edges is V*(V-1).

On the other hand, in a simple undirected graph, each edge is bidirectional (it goes both ways). So, for a graph with V vertices, each vertex can have an edge to V-1 other vertices. However, because each edge is counted twice (once for each direction), the maximum number of edges is V*(V-1)/2.

If graph is dense, E approx to V^2.

Dense means as much as edges possible.

We can have more edges if the graph is directed. For example V1 ----->  V2
                                                                <-----  
If the graph is undirected, this si gonna look like this:  V1 ----- V2. 