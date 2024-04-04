class Node:
    
    def __init__(self, data=None|str, size = 27) -> None: # 27 for lowercase letter mapping (53 if uppercase included)
        # data payload
        self.data = data
        #* index 0 is for the terminal node. ASCII value of char maps to the array indices[1-26].
        #? we store the data in the terminal node
        #! the array index corresponds to the "link" aka a character in the trie
        self.link: list = [None] * size
        #* freq indicates how many words in trie contain prefix (upto char represented by this node)
        self.freq = 0
        #* unique freq indicates how many unique words are in the trie
        self.unique_freq = 0


class Trie:
    '''
    Trie is a type of k-ary search tree used for storing and searching a specific (string) key from a set. 
    Using Trie, search complexities can be brought to optimal worst case: O (N) where N is the length of key. O(1) best case when first char not in trie
    '''

    def __init__(self):
        self.root: Node = Node()


    def insert_recur(self,key, data ):
        self.insert_recur_aux(self.root,key,data)
    
    def insert_recur_aux(self, current_node,key,data):

        # base case
        if not key:
            if current_node.link[0] is not None:
                raise Exception(f"Key already exists!")
            current_node.link[0] = Node()
            #* store data in the terminal node
            current_node.link[0].data = data
            return
        
        # recursive case
        index = ord(key[0]) -ord('a') + 1
        if current_node.link[index] is None:
            current_node.link[index] = Node()
        self.insert_recur_aux(current_node.link[index],key[1:],data)


    def search_recur(self, key):
        return self.search_recur_aux(self.root,key)
    

    def search_recur_aux(self, current_node, key):
        if not key:
            # current node is now the terminal node.
            if current_node.link[0] is None:
                raise Exception("Key does not exist!")
            return current_node.link[0].data

        index = ord(key[0]) - ord('a') + 1
        if current_node.link[index] is None:
            raise Exception("Key does not exist!")
        return self.search_recur_aux(current_node.link[index], key[1:])




if __name__ == "__main__":
    pass
















