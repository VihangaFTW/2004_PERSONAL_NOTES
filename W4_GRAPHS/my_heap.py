from typing import Generic
from my_array import ArrayR, T
from math import inf


class MinHeap(Generic[T]):
    '''
    Custom MinHeap class for dijkstra algorithm. Takes only Vertex objects as inputs.
    Min heap property: Parent node is smaller/equals than its children.
    Heap is filled from left to right per level.
    Items are stored from index 1 in the array to make the heap arithmetic easier.
    '''
    #! ArrayR cannot handle length <= 0
    MIN_CAPACITY = 1

    def __init__(self, max_size: int) -> None:
        self.length = 0
        self.arr = ArrayR(max(self.MIN_CAPACITY,max_size)+1)

    def __len__(self) -> int:
        return self.length
    
    def is_full(self) -> bool:
        return self.length+1 == len(self.arr)

    def _smallest_child(self,elem_index)-> int:
        '''
        This helper function returns the index of the smallest child node, given the index 
        of the parent node.
        : elem_index:- index of the parent node
        : returns the index of the smallest child node
        : time comp:- O(1) in all cases
        '''
        #! check whether the left child is the last node in heap first, 
        #! otherwise we will run into IndexError when we check the right child
        if 2*elem_index == self.length or \
            self.arr[2*elem_index] <= self.arr[2*elem_index+1]:
            return 2*elem_index
        else:
            return 2*elem_index +1

    
    def _sink(self, elem_index: int) -> None:
        '''
        This method sinks the node at given index downthe heap to its correct position so that the 
        heap property is maintained. Used when the root node is removed in get_min method.
        : elem_index: index of node that need to be repositioned down the
        . heap
        : returns None
        : time comp:- worst case is O(log N) where N is the number of nodes in the heap
                      best case is  O(1) when the node is swapped with its child node once.
        : space comp:- both O(1) as nodes are just repositioned
        '''
        item = self.arr[elem_index]
        self._sink_aux(elem_index,item)

        
    def _sink_aux(self,elem_index:int, item: tuple[int,object]) -> None:
        
        #* sink is used in the get_min operation. We decrement the length before performing sink there.
        #* So the check should be elem_index*2 > self.length not elem_index*2 == self.length.
        #* This is because when we decrement length, the second last node becomes the last node in heap
        #* if we use == operator, this last node would not be compared with its parent node

        if elem_index*2 > self.length or self.arr[elem_index*2][0] > self.arr[elem_index][0]:
            return 
        else:
            smallest_child_idx = self._smallest_child(elem_index)
            self.arr[elem_index], self.arr[smallest_child_idx] = self.arr[smallest_child_idx], self.arr[elem_index]
            #* update mapping of heap- array index for each Vertex after swap
            self.arr[elem_index][1].array_index, self.arr[smallest_child_idx][1].array_index = self.arr[smallest_child_idx][1].array_index, self.arr[elem_index][1].array_index
            self._sink_aux(smallest_child_idx,item)


    def _rise(self, elem_index: int)-> None:
        '''
        This method rises the node at given index up the heap to its correct position so that the 
        heap property is maintained.
        : elem_index: index of node that need to be repositioned up the heap
        : returns None
        : time comp:- worst case is O(log N) where N is the number of nodes in the heap
                      best case is  O(1) when the node is swapped with its parent node once.
        : space comp:- both O(1) as nodes are just repositioned
        '''
        item = self.arr[elem_index]
        self._rise_aux(elem_index, item)

    def _rise_aux(self,elem_index: int,item:tuple[int,object]) -> None:
        '''
        Recursive helper method for rise operation.
        '''
        if elem_index == 1 or self.arr[elem_index][0] > self.arr[elem_index//2][0]:
            self.arr[elem_index] = item
        else:
            self.arr[elem_index],self.arr[elem_index//2] = self.arr[elem_index//2], self.arr[elem_index]
            #* update mapping of heap- array index for each Vertex after swap
            self.arr[elem_index][1].array_index, self.arr[elem_index//2][1].array_index = \
                self.arr[elem_index//2][1].array_index, self.arr[elem_index][1].array_index
            self._rise_aux(elem_index//2, item)


    def add(self, distance: T, item: object) -> None:
        '''
        This method adds an element as a node at the end of the heap.
        : item: item to be added to the heap
        : retuns None
        : raises Exception if the heap is empty.
        : time comp:-  worst is O(log N) due to rise operation comp
                       best is O(1) due to rise opertion comp

        '''
        if self.is_full():
            raise Exception("Heap is full!")
        # items are stored from indices[1....self.length]
        self.length += 1
        #* update mapping of heap- array index for Vertex 
        item.array_index = self.length
        self.arr[self.length] = (distance,item)
        self._rise(self.length)

    def get_min(self)-> tuple[int,object]:
        '''
        Retrieve the element at the top of the heap.
        : returns the element at the top of the heap.
        : raises Exception if the heap is empty.
        : time comp:- worst is O(log N) due to sink operation comp
                      best is O(1) due to sink operation comp
        : space comp: O(1) as elements are just repositioned
        '''
        if self.length == 0:
            raise Exception("Heap is empty!")
        
        item = self.arr[1]
        self.length -= 1
        if self.length > 0:
            self.arr[1], self.arr[self.length+1] = self.arr[self.length+1], self.arr[1]
            #* update mapping of heap- array index for each Vertex after swap
            self.arr[1][1].array_index, self.arr[self.length+1][1].array_index = \
                self.arr[self.length+1][1].array_index, self.arr[1][1].array_index
            self._sink(1)
        return item
    
    #! for Vertex objects only
    def update(self, vertex: object, new_distance: int) -> None:
        vertex_index = vertex.array_index
        self.arr[vertex_index] = (new_distance,vertex)
        parent_node_idx = vertex_index//2
        if parent_node_idx > 0 and self.arr[parent_node_idx][0] > new_distance:
            # if the updated value is smaller than its parent, perform a rise operation
            self._rise(vertex_index)
        else:
            # otherwise, perform a sink operation
            self._sink(vertex_index)


    def __str__(self)-> str:
        return_string = ""
        for i in range(1,self.length+1):
            return_string += f'Item at index {i} is ({self.arr[i][0]}, {self.arr[i][1].id})\n' \
            + f"MAPPING: Vertex index is {self.arr[i][1].array_index}\n"

        return return_string

if __name__ == "__main__":
    pass


