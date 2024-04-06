from __future__ import annotations
from typing import TypeVar,Generic
from abc import ABC,abstractmethod

T = TypeVar("T")

class Set(ABC, Generic[T]):
    
    def __init__(self)-> None:
        self.size = 0


    def __len__(self)->int:
        return self.size
    
    @abstractmethod
    def union(self, other_set: Set[T]):
        pass

    @abstractmethod
    def add(self, element: T) -> None:
        pass


class DisjointedSet(Set):

    def __init__(self, max_size:int) -> None:
        super().__init__()
        # at first, there is only one element so that's the root. Hence -1.
        #* In the parent array, a negative sign indicates the root. The number after the - indicates the size of the tree.
        self.parent_arr = [-1] * max_size
        self.last_index = 0


    def add(self, element: Vertex) -> None:
        '''
        Function to add an element to the set.
        Basically, this function maps the parent array index to the vertex's attribute for O(1) traversal up a tree.
        : element: Vertex object that is to be added to the Disjointed Set.
        : returns None.
        : time comp: O(1)
        : space comp: O(1)
        '''
        if self.size + 1 > len(self.parent_arr):

            raise ValueError("Set is full!")
        
        element.parent_array_index = self.last_index
        self.last_index += 1
        self.size += 1

    def find(self, element: Vertex) -> tuple[int,int]:
        '''
        Helper function for union method that traverses up the parents in a tree/set
        until it find the root. The element at the corresponding index in the parent
        array will contain the negated size of the tree/set.
        : element: the source of traversal 
        : return: a tuple consisting of the index of root in parent array and size of tree/set
        : time comp: O(log V) where V is the number of vertices in the set
        '''
        # negative means this is the root of the tree
        if self.parent_arr[element.parent_array_index] < 0:
            return element.parent_array_index,self.parent_arr[element.parent_array_index] *-1 
        # positive means has parent
        else:
            return self.find(self.parent_arr[element.parent_array_index])
            

    def union(self, vertex: Vertex, other_vertex: Vertex)-> bool:
        # retrieve the index and 
        index1,size1 = self.find(vertex)
        index2,size2 = self.find(other_vertex)
        if index1 != index2:
            #* more efficient to add to bigger set/tree
            if size1 >= size2:
                self.parent_arr[index2] = index1
                # update the vertex parent array index pointer
                other_vertex.parent_array_index = index1
                # update the size of tree/set after union
                self.parent_arr[index1] = -(size1+size2)
                return True
            else:
                self.parent_arr[index1] = index2
                # update the vertex parent array index pointer
                vertex.parent_array_index = index2
                # update the size of tree/set after union
                self.parent_arr[index2] = -(size1+size2)
                return True
        return False

