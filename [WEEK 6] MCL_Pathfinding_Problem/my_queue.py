from abc import ABC,abstractmethod
from typing import TypeVar,Generic

from my_array import ArrayR


T = TypeVar('T')

class Queue(ABC, Generic[T]):
    """ Abstract class for a generic Queue. """

    def __init__(self) -> None:
        # size of queue not array
        self.size = 0

    @abstractmethod
    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue."""
        pass

    @abstractmethod
    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the queue."""
        return self.length

    def clear(self):
        """ Clears all elements from the queue. """
        self.length = 0

class CircularQueue(Queue[T]):

    def __init__(self, length: int) -> None:
        Queue.__init__(self)
        self.elements = ArrayR(length)
        self.front = 0
        self.back = 0
    
    def serve(self) -> T:
        if self.size == 0:
            raise ValueError("Queue is empty!")
        serve = self.elements[self.front]
        self.size -= 1
        self.front = (self.front+1) % len(self.elements)
        return serve
    
    def append(self, item: T) -> None:
        if len(self.elements) == self.size:
            raise ValueError("Queue is full!")
        self.elements[self.back] = item
        self.size += 1
        self.back =  (self.back+1) % len(self.elements)

    def __len__(self) -> int:
        return self.size
    
    def __str__(self) -> str:
        
        return_str = "A Queue with the following elements:\n"
        if self.size == 0:
            return "A Queue with no elements"
        
        for i in range(self.size):
            index = (self.front + i) % len(self.elements)
            return_str += str(self.elements[index]) + "\n"
        return return_str
    

if __name__ == "__main__":
    my_queue = CircularQueue(1)
    my_queue.append(1)
    #my_queue.append(2)
    print(my_queue)
    my_queue.serve()
    print(my_queue)
