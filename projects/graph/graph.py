"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        temp = []
        #make queue
        queue = Queue()
        #visited set
        visited = set()
        #put starting in queue
        queue.enqueue(starting_vertex)
        #while not empty, dequeue item, and mark item as visited
        while queue.size():
            node = queue.dequeue()
            visited.add(node)
            temp.append(node)
            #for each dequeued item edges, place in queue if not visited
            for edge in self.vertices[node]:
                if edge not in visited:
                    queue.enqueue(edge)
        print(temp)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        temp = []
        #make stack
        stack = Stack()
        #visited set
        visited = set()
        #put starting in stack
        stack.push(starting_vertex)
        #while not empty, pop item, and mark item as visited
        while stack.size():
            node = stack.pop()
            visited.add(node)
            temp.append(node)
            #for each popped item edges, place in stack if not visited
            for edge in self.vertices[node]:
                if edge not in visited:
                    visited.add(edge)
                    stack.push(edge)
        print(temp)

    def dft_recursive(self, starting_vertex, path=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        #add starting index to path
        path += [starting_vertex]
        
        #for the neighboring node, if the neighbor is not present recursivly add it to the path
        for next in self.vertices[starting_vertex]:
            if next not in path:
                path = self.dft_recursive(next, path)
        return path

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create queue, visited flag and add the starting vertex to the queue
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        #while not empty, dequeue and place in path
        #record the vertex as the last item in the path
        while q.size():
            path = q.dequeue()
            vertex = path[-1]
            #if the vertex is equal to the destination return the path
            if vertex == destination_vertex:
                return path
            #if the vertex has not been visited
            elif vertex not in visited:
                #for each item in the current path
                for next in self.vertices[vertex]:
                    #create a copy of the old path, append the next item to this new path, and add the new path to the queue
                    new_path = list(path)
                    new_path.append(next)
                    q.enqueue(new_path)
                #mark vertex as visited
                visited.add(vertex)
        #edge case if destination_vertex is not found
        if vertex != destination_vertex:
            return f"path from {starting_vertex} to {destination_vertex} not found"
        return path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #make stack
        s = Stack()
        #visited set
        visited = set()
        #put starting in stack
        s.push([starting_vertex])
        #while not empty, pop item, and mark item as visited
        while s.size():
            path = s.pop()
            vertex = path[-1]
            #if the vertex is equal to the destination return the path
            if vertex == destination_vertex:
                return path
            #if the vertex has not been visited
            elif vertex not in visited:
                #for each item in the current path
                for next in self.vertices[vertex]:
                    #create a copy of the old path, append the next item to this new path, and add the new path to the queue
                    new_path = list(path)
                    new_path.append(next)
                    s.push(new_path)
                #mark vertex as visited
                visited.add(vertex)
        #edge case if destination_vertex is not found
        if vertex != destination_vertex:
            return f"path from {starting_vertex} to {destination_vertex} not found"
        return path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print(graph.bfs(1, 16))
    print(graph.bfs(3, 3))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs(3, 26))
    print(graph.dfs(2, 2))